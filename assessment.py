def show_frames(frames, frame_size):
    display = frames[:]
    while len(display) < frame_size:
        display.append('-')
    return display

def lru(pages, frame_size):
    frames = []
    recent = {}      
    time = 0
    hits = 0
    misses = 0

    print("LRU Simulation")

    for p in pages:
        time += 1
        print(f"\nPage → {p}")

        if p in frames:
            hits += 1
            recent[p] = time
            print("HIT →", show_frames(frames, frame_size))
            continue

        misses += 1

        if len(frames) < frame_size:
            frames.append(p)
            recent[p] = time
            print("MISS →", show_frames(frames, frame_size))
            continue

        lru_page = min(recent, key=recent.get)
        frames[frames.index(lru_page)] = p
        del recent[lru_page]
        recent[p] = time

        print(f"MISS (replaced {lru_page}) →", show_frames(frames, frame_size))

    print("\nTotal Hits:", hits)
    print("Total Misses:", misses)
    print("Hit Ratio:", hits / len(pages))

pages = list(map(int, input("Enter page reference string: ").split()))
frame_size = int(input("Enter number of frames: "))
lru(pages, frame_size)
