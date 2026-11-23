from pathlib import Path
import shutil


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    src = Path(__file__).resolve().parent / "entry.png"
    dst = output_dir / "entry.png"
    
    shutil.copy2(src, dst)


if __name__ == "__main__":
    main()
