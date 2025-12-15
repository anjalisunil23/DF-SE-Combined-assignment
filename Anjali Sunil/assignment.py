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
    for i in range(len(pages)):
        p = pages[i]

        if p not in memory:
            page_faults += 1

            if len(memory) < frames:
                memory.append(p)
            else:
                # Find least recently used page
                lru_index = 0
                min_time = float('inf')

                for j in range(len(memory)):
                    if memory[j] in pages[:i]:
                        last_used = pages[:i][::-1].index(memory[j])
                    else:
                        last_used = float('inf')

                    if last_used < min_time:
                        min_time = last_used
                        lru_index = j

                memory[lru_index] = p

        print(f"Page {p}: {memory}")

    return page_faults


def main():
    while True:
        print("\n====================================")
        print("   PAGE REPLACEMENT ALGORITHMS MENU")
        print("====================================")
        print("1. FIFO")
        print("2. LRU")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting program.")
            break

        pages = list(map(int, input("Enter page reference string: ").split()))
        frames = int(input("Enter number of frames: "))

        if choice == '1':
            faults = fifo(pages, frames)
            print(f"Total Page Faults (FIFO): {faults}")

        elif choice == '2':
            faults = lru(pages, frames)
            print(f"Total Page Faults (LRU): {faults}")

        else:
            print("Invalid choice! Please enter 1-3.")


if __name__ == "__main__":
    main()


       
