# Authored By EchoX Networks © 2025
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

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO
    
    try:
        repo = Repo()
        LOGGER(__name__).info(f"Git Client Found [VPS DEPLOYER]")
    except (GitCommandError, InvalidGitRepositoryError):
        LOGGER(__name__).warning("Git repository not found or git command failed. Skipping auto-update.")
        return

    try:
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)

        LOGGER(__name__).info(f"Fetching updates from upstream repository...")
        origin.fetch()
        
        repo.create_head(
            config.UPSTREAM_BRANCH,
            origin.refs[config.UPSTREAM_BRANCH],
        )
        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)
        
        nrs = repo.remote("origin")
        nrs.pull(config.UPSTREAM_BRANCH)
        
        LOGGER(__name__).info(f"Successfully updated from upstream.")
    except Exception as e:
        LOGGER(__name__).error(f"Failed to fetch updates from git: {e}")
