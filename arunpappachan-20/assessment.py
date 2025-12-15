def fifo_cache_analysis(reference_string, cache_size):
    cache = []
    hits = 0
    misses = 0

    print("FIFO Cache Analysis")
    print("Cache Size:", cache_size)
    print("Reference String:", reference_string)
    print("-" * 50)

    for i, block in enumerate(reference_string, start=1):
        print(f"Step {i}: Accessing block {block}")

        if block in cache:
            hits += 1
            print("Result: HIT")
        else:
            misses += 1
            print("Result: MISS")

            if len(cache) < cache_size:
                cache.append(block)
            else:
                removed = cache.pop(0)   
                cache.append(block)
                print(f"Removed block: {removed}")

        print("Cache State:", cache)
        print("-" * 50)

    hit_ratio = hits / (hits + misses)

    print("\nFinal Analysis")
    print("Total Hits:", hits)
    print("Total Misses:", misses)
    print("Hit Ratio:", round(hit_ratio, 2))



reference_string = [1, 2, 3, 1, 4, 5, 2, 1]
cache_size = 3

fifo_cache_analysis(reference_string, cache_size)
