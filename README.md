
# 2D Path Finder – TetraMem Take-Home Challenge

This repository contains a solution to the 2D pathfinding problem for TetraMem’s take-home interview challenge. The goal is to find paths that only pass through black pixels in a given image.

## 🧠 Problem Summary

- Input: A 2D black-and-white image and two pairs of start/end coordinates.
- Task:
  1. Determine if a valid path exists between each start/end pair using only black pixels.
  2. Ensure that both paths (if they exist) do not intersect.
  3. Visualize each valid path on the image and save it.

## 🚀 How to Run

Make sure you have the following libraries installed:

```bash
pip install numpy pillow imageio
```

Then, place your input image (e.g., `universe1.png`) in the same directory and run:

```bash
python path_finder.py
```

## 📁 Files

- `path_finder.py`: Main script with pathfinding logic.
- `bars_path1.png`, `bars_path2.png`: Visualized paths for `bars.png`.
- `polygons_path1.png`: Visualized path for `polygons.png`. Second path does not exist.
- `ring_path1.png`, `ring_path2.png`: Paths for `small-ring.png` (start = end).

## ✅ Results Summary

| Image            | Path 1 Exists | Path 2 Exists | Disjoint | Notes                        |
|------------------|----------------|----------------|-----------|------------------------------|
| `bars.png`       | ✅              | ✅              | ❌         | Paths overlap                |
| `polygons.png`   | ✅              | ❌              | ❌         | Second path not found        |
| `small-ring.png` | ✅              | ✅              | ❌         | Both paths are 1-pixel long  |

## 🧩 Notes

- Paths are visualized in red.
- 4-connectivity is used (up/down/left/right).
- Only black pixels (value < 128) are considered traversable.

