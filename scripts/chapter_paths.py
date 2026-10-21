"""Locations and legacy-aware source expansion for the standalone chapter."""

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapter"
STEM = "ESQC_Loos_HF_BF_chapter"
FILES = (f"chapter/{STEM}.tex",)


def required_assets():
    """Resolve literal graphics and portrait-macro arguments in the one source."""
    text = (CHAPTER / f"{STEM}.tex").read_text()
    # Commented-out illustrations are not compilation or submission inputs.
    # Keep escaped percent signs, which are ordinary TeX text.
    text = re.sub(r"(?<!\\)%[^\n]*", "", text)
    names = set()
    for name in re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", text):
        if "#" not in name:
            names.add(name if name.startswith("figures/") else "figures/" + name)
    names.update(re.findall(r"figures/sketch-[a-z-]+\.png", text))
    paths = []
    for name in sorted(names):
        path = CHAPTER / name
        if not path.suffix:
            candidates = [path.with_suffix(ext) for ext in (".pdf", ".png", ".jpg", ".jpeg")
                          if path.with_suffix(ext).is_file()]
            if len(candidates) != 1:
                raise ValueError(f"Ambiguous or missing graphic: {name}")
            path = candidates[0]
        if not path.is_file():
            raise ValueError(f"Missing chapter graphic: {path}")
        paths.append(path)
    return paths


def revision_source(ref):
    """Read a monolithic or pre-consolidation revision, expanding local inputs."""
    def read(name):
        return subprocess.check_output(
            ["git", "show", f"{ref}:{name}"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL,
        )

    def expand(name, ancestors=()):
        if name in ancestors:
            raise ValueError(f"Recursive chapter input: {name}")

        def include(match):
            target = match[1]
            if not Path(target).suffix:
                target += ".tex"
            return "\n" + expand(target, (*ancestors, name)) + "\n"

        return re.sub(r"\\input\{([^}]+)\}", include, read(name))

    try:
        return read(FILES[0])
    except subprocess.CalledProcessError:
        return expand(f"{STEM}.tex")
