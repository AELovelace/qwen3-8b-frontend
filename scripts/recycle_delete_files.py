from __future__ import annotations

import argparse
import ctypes
import sys
import time
from pathlib import Path

FO_DELETE = 3
FOF_SILENT = 0x0004
FOF_NOCONFIRMATION = 0x0010
FOF_ALLOWUNDO = 0x0040
FOF_NOERRORUI = 0x0400


class SHFILEOPSTRUCTW(ctypes.Structure):
    _fields_ = [
        ("hwnd", ctypes.c_void_p),
        ("wFunc", ctypes.c_uint),
        ("pFrom", ctypes.c_wchar_p),
        ("pTo", ctypes.c_wchar_p),
        ("fFlags", ctypes.c_ushort),
        ("fAnyOperationsAborted", ctypes.c_bool),
        ("hNameMappings", ctypes.c_void_p),
        ("lpszProgressTitle", ctypes.c_wchar_p),
    ]


shell32 = ctypes.windll.shell32


def move_to_recycle_bin(path: Path) -> None:
    if not path.is_file():
        return

    source = str(path.resolve()) + "\0\0"
    operation = SHFILEOPSTRUCTW()
    operation.wFunc = FO_DELETE
    operation.pFrom = source
    operation.fFlags = (
        FOF_ALLOWUNDO
        | FOF_NOCONFIRMATION
        | FOF_NOERRORUI
        | FOF_SILENT
    )

    result = shell32.SHFileOperationW(ctypes.byref(operation))
    if result != 0:
        raise OSError(f"SHFileOperationW failed for {path} with code {result}")
    if operation.fAnyOperationsAborted:
        raise OSError(f"Recycle Bin operation aborted for {path}")


def sweep_directory(directory: Path) -> int:
    recycled = 0
    for path in directory.iterdir():
        if path.is_file() and path.name.endswith(".delete"):
            try:
                move_to_recycle_bin(path)
                recycled += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Recycled: {path.name}", flush=True)
            except Exception as exc:
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failed: {path.name}: {exc}", file=sys.stderr, flush=True)
    return recycled


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Every 15 seconds, send *.delete files in the current working directory to the Recycle Bin."
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=15.0,
        help="Seconds between directory sweeps (default: 15)",
    )
    return parser.parse_args()


def main() -> int:
    if sys.platform != "win32":
        print("This script only supports Windows.", file=sys.stderr)
        return 1

    args = parse_args()
    watch_dir = Path.cwd()

    print(
        f"Watching {watch_dir} for files ending in .delete every {args.interval:g} seconds. Press Ctrl+C to stop.",
        flush=True,
    )

    try:
        while True:
            sweep_directory(watch_dir)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Stopped.", flush=True)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
