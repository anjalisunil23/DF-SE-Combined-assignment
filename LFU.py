def lfu(pages, capacity):
    memory = []
    freq = {}
    faults = 0

    for p in pages:
        print("\nPage requested:", p)


        if p in memory:
            freq[p] += 1
        else:
            faults += 1
            print("Page Fault!")


            if len(memory) < capacity:
                memory.append(p)
                freq[p] = 1
            else:

                least_freq = min(freq.values())


                for page in memory:
                    if freq[page] == least_freq:
                        remove_page = page
                        break


                memory.remove(remove_page)
                del freq[remove_page]


                memory.append(p)
                freq[p] = 1

        print("Memory:", memory)
        print("Frequency:", freq)

    print("\nTotal Page Faults =", faults)
pages = [2, 3, 2, 1, 5, 2, 4, 5]
capacity = 3

lfu(pages, capacity)
