def fifo_cache(blocks, cache_size):
    cache = []
    hits = 0
    misses = 0

    for block in blocks:
        print(f"Accessing block: {block}")

        if block in cache:
            hits += 1
            print("→ HIT")
        else:
            misses += 1
            print("→ MISS")

            if len(cache) < cache_size:
                cache.append(block)
            else:
                cache.pop(0)     
                cache.append(block)

        print("Cache:", cache)
        print("----------------")

    hit_ratio = hits / (hits + misses)
    print("Total Hits:", hits)
    print("Total Misses:", misses)
    print("Hit Ratio:", hit_ratio)


blocks = [1, 2, 3, 1, 4, 5, 2, 1]
cache_size = 3

fifo_cache(blocks, cache_size)
