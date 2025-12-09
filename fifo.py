def fifo_cache_simulation(cache_size, references):
    cache = []
    hits = 0
    misses = 0
    replace_index = 0  # FIFO pointer

    print("FIFO Cache Simulation")
    print("----------------------")
    for block in references:

        print(f"\nReference: {block}")

        if block in cache:
            hits += 1
            print("Status: HIT")
        else:
            misses += 1
            print("Status: MISS")

            if len(cache) < cache_size:
                cache.append(block)
            else:
                cache[replace_index] = block
                replace_index = (replace_index + 1) % cache_size

        print(f"Cache: {cache}")

    hit_ratio = hits / (hits + misses)

    print("\n--- Final Results ---")
    print(f"Total Hits: {hits}")
    print(f"Total Misses: {misses}")
    print(f"Hit Ratio: {hit_ratio:.2f}")
# Sample execution
cache_size = 3
references = [1, 2, 3, 2, 4, 1, 5, 2, 3]

fifo_cache_simulation(cache_size, references)
