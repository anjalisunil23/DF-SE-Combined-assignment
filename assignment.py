def fifo(pages, frames):
    memory = []
    page_faults = 0
    index = 0

    print("\n--- FIFO Page Replacement ---")
    for p in pages:
        if p not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(p)
            else:
                memory[index] = p
                index = (index + 1) % frames
        print(f"Page {p}: {memory}")
    return page_faults


def lru(pages, frames):
    memory = []
    page_faults = 0

    print("\n--- LRU Page Replacement ---")
    for i, p in enumerate(pages):
        if p not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(p)
            else:
                # Find LRU page
                last_used = []
                for m in memory:
                    if m in pages[:i]:
                        last_used.append(pages[:i][::-1].index(m))
                    else:
                        last_used.append(float('inf'))
                replace_index = last_used.index(max(last_used))
                memory[replace_index] = p
        print(f"Page {p}: {memory}")
    return page_faults


def optimal(pages, frames):
    memory = []
    page_faults = 0

    print("\n--- Optimal Page Replacement ---")
    for i, p in enumerate(pages):
        if p not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(p)
            else:
                future_use = []
                for m in memory:
                    if m in pages[i+1:]:
                        future_use.append(pages[i+1:].index(m))
                    else:
                        future_use.append(float('inf'))
                replace_index = future_use.index(max(future_use))
                memory[replace_index] = p
        print(f"Page {p}: {memory}")
    return page_faults


# -----------------------------------------
# Menu-Driven Program
# -----------------------------------------

def main():
    while True:
        print("\n====================================")
        print("   PAGE REPLACEMENT ALGORITHMS MENU")
        print("====================================")
        print("1. FIFO")
        print("2. LRU")
        print("3. Optimal")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting program.")
            break

        # Input section
        pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
        frames = int(input("Enter number of frames: "))

        if choice == '1':
            faults = fifo(pages, frames)
            print(f"Total Page Faults (FIFO): {faults}")

        elif choice == '2':
            faults = lru(pages, frames)
            print(f"Total Page Faults (LRU): {faults}")

        elif choice == '3':
            faults = optimal(pages, frames)
            print(f"Total Page Faults (Optimal): {faults}")

        else:
            print("Invalid choice! Please enter 1-4.")


# Run the program
if __name__ == "__main__":
    main()
