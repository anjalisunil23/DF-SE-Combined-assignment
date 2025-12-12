from collections import defaultdict

def show_frames(frames, frame_size):
    display = frames[:]  # copy
    while len(display) < frame_size:
        display.append('-')
    return display

def fifo(pages, frame_size):
    frames = []
    faults = 0

    print("\nFIFO Simulation")
    for step, page in enumerate(pages, start=1):
        if page in frames:
            print(f"Step {step} → Page {page} → HIT  → Frames: {show_frames(frames, frame_size)}")
        else:
            faults += 1
            if len(frames) < frame_size:
                frames.append(page)
                print(f"Step {step} → Page {page} → MISS → Frames: {show_frames(frames, frame_size)}")
            else:
                evicted = frames.pop(0)
                frames.append(page)
                print(f"Step {step} → Page {page} → MISS (evicted {evicted}) → Frames: {show_frames(frames, frame_size)}")

    hits = len(pages) - faults
    print_summary(faults, hits, len(pages))


def lru(pages, frame_size):
    frames = []
    faults = 0

    print("\nLRU Simulation")
    for step, page in enumerate(pages, start=1):
        if page in frames:
            frames.remove(page)
            frames.append(page)
            print(f"Step {step} → Page {page} → HIT  → Frames: {show_frames(frames, frame_size)}")
        else:
            faults += 1
            if len(frames) < frame_size:
                frames.append(page)
                print(f"Step {step} → Page {page} → MISS → Frames: {show_frames(frames, frame_size)}")
            else:
                evicted = frames.pop(0)
                frames.append(page)
                print(f"Step {step} → Page {page} → MISS (evicted {evicted}) → Frames: {show_frames(frames, frame_size)}")

    hits = len(pages) - faults
    print_summary(faults, hits, len(pages))


def lfu(pages, frame_size):
    frames = []
    freq = defaultdict(int)
    insert_time = {}
    time = 0
    faults = 0

    print("\nLFU Simulation")
    for step, page in enumerate(pages, start=1):
        time += 1
        freq[page] += 1

        if page in frames:
            print(f"Step {step} → Page {page} → HIT  → Frames: {show_frames(frames, frame_size)}")
        else:
            faults += 1
            if len(frames) < frame_size:
                frames.append(page)
                insert_time[page] = time
                print(f"Step {step} → Page {page} → MISS → Frames: {show_frames(frames, frame_size)}")
            else:
                victim = min(frames, key=lambda p: (freq[p], insert_time[p]))
                frames.remove(victim)
                frames.append(page)
                insert_time[page] = time
                print(f"Step {step} → Page {page} → MISS (evicted {victim}) → Frames: {show_frames(frames, frame_size)}")

    hits = len(pages) - faults
    print_summary(faults, hits, len(pages))

def print_summary(faults, hits, total):
    print("\nPage Faults =", faults)
    print("Hits        =", hits)
    print(f"Hit Ratio   = {hits}/{total} = {hits/total:.2f}")


while True:
    print("   PAGE REPLACEMENT MENU")
    print("1. FIFO")
    print("2. LRU")
    print("3. LFU")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Exiting...")
        break

    pages = list(map(int, input("Enter reference string (space-separated): ").split()))
    frame_size = int(input("Enter number of frames: "))

    if choice == "1":
        fifo(pages, frame_size)
    elif choice == "2":
        lru(pages, frame_size)
    elif choice == "3":
        lfu(pages, frame_size)
    else:
        print("Invalid choice! Try again.")
