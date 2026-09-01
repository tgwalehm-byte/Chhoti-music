import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()

        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(
        install_requirements()
    )


def git():
    REPO_LINK = (config.UPSTREAM_REPO or "").strip()

    # Normalize repository URL
    if REPO_LINK.endswith(".git"):
        REPO_LINK = REPO_LINK[:-4]

    if config.GIT_TOKEN:
        # GitHub repository URL:
        # https://github.com/reetsingh886/criminammusic
        if "github.com/" in REPO_LINK:
            repo_path = REPO_LINK.split("github.com/", 1)[1].strip("/")
            UPSTREAM_REPO = (
                f"https://{config.GIT_TOKEN}@github.com/{repo_path}.git"
            )
        else:
            # Invalid/non-GitHub URL: use it directly instead of crashing
            UPSTREAM_REPO = REPO_LINK
    else:
        UPSTREAM_REPO = REPO_LINK

    try:
        repo = Repo()
        LOGGER(__name__).info(
            "» ɢɪᴛ ᴄʟɪᴇɴᴛ ғᴏᴜɴᴅ [ᴠᴘs ᴅᴇᴘʟᴏʏᴇʀ]"
        )

    except GitCommandError:
        LOGGER(__name__).info(
            "» ɪɴᴠᴀʟɪᴅ ɢɪᴛ ᴄᴏᴍᴍᴀɴᴅ"
        )

    except InvalidGitRepositoryError:
        repo = Repo.init()

        if "origin" in repo.remotes:
            origin = repo.remote("origin")
            origin.set_url(UPSTREAM_REPO)
        else:
            origin = repo.create_remote(
                "origin",
                UPSTREAM_REPO,
            )

        origin.fetch()

        repo.create_head(
            config.UPSTREAM_BRANCH,
            origin.refs[config.UPSTREAM_BRANCH],
        )

        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )

        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

        try:
            repo.create_remote(
                "origin",
                config.UPSTREAM_REPO,
            )
        except BaseException:
            pass

        nrs = repo.remote("origin")
        nrs.fetch(config.UPSTREAM_BRANCH)

        try:
            nrs.pull(config.UPSTREAM_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")

        install_req(
            "pip3 install --no-cache-dir -r requirements.txt"
        )

        LOGGER(__name__).info(
            "» ꜰᴇᴛᴄʜɪɴɢ ᴜᴘᴅᴀᴛᴇs ꜰʀᴏᴍ ᴜᴘsᴛʀᴇᴀᴍ ʀᴇᴘᴏsɪᴛᴏʀʏ..."
        )
