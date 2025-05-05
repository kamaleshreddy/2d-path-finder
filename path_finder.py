
import numpy as np
import imageio.v3 as imageio
from collections import deque
from PIL import Image, ImageDraw

def find_path(universe: np.ndarray, start, end):
    h, w = universe.shape
    visited = np.full((h, w), False)
    parent = {}

    q = deque()
    q.append(start)
    visited[start[1]][start[0]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and universe[ny][nx] == 0:
                visited[ny][nx] = True
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))
    return None

def visualize_path(image_array, path, output_filename):
    img = Image.fromarray(image_array)
    draw = ImageDraw.Draw(img)
    for x, y in path:
        draw.point((x, y), fill=(255, 0, 0))
    img.save(output_filename)

def are_paths_disjoint(path1, path2):
    return set(path1).isdisjoint(set(path2))

def prepare_binary_image(img_array):
    if len(img_array.shape) == 3:
        gray_img = np.mean(img_array[:, :, :3], axis=2).astype(np.uint8)
    else:
        gray_img = img_array
    return np.where(gray_img < 128, 0, 1)

if __name__ == "__main__":
    img = imageio.imread("universe1.png")
    binary = prepare_binary_image(img)

    start1, end1 = (10, 10), (90, 90)
    start2, end2 = (100, 20), (150, 80)

    path1 = find_path(binary, start1, end1)
    path2 = find_path(binary, start2, end2)

    if path1:
        visualize_path(np.array(img), path1, "path1_visualized.png")
    if path2:
        visualize_path(np.array(img), path2, "path2_visualized.png")

    if path1 and path2:
        disjoint = are_paths_disjoint(path1, path2)
        print("Both paths exist. Are they disjoint?", disjoint)
    else:
        print("One or both paths do not exist.")
