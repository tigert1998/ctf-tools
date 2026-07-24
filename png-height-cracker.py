import zlib
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser("PNG true height cracker")
    parser.add_argument("--path")
    args = parser.parse_args()

    with open(args.path, "rb") as f:
        data = f.read()
    crc_gt = data[29:33]
    data = data[12:29]
    original_h = int.from_bytes(data[8:12])
    print(f"PNG original height: {original_h}")
    for h in range(1, 10000):
        data = data[:8] + h.to_bytes(4) + data[12:]
        crc = zlib.crc32(data) & 0xFFFFFFFF
        if crc.to_bytes(4) == crc_gt:
            print(f"PNG true height: {h}")
            break
