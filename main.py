"""Lens Island Desktop — A local helper for Len's Island homestead folders, voxel builds, and island photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='lens_island_desktop',
        description="A local helper for Len's Island homestead folders, voxel builds, and island photos.",
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Lens Island Desktop')
    print('Keep the homestead on disk before a build patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
