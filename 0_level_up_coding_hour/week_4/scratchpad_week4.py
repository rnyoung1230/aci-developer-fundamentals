# Week 4 Assessment Question
sizes_avail = {'S', 'M', 'L', 'XL', 'XXL'}
sizes_needed = {'XS', 'S', 'M', 'L', 'XL', 'XXL'}


print(f"Answer 1: {sizes_needed.issubset(sizes_avail)}")

print(f"Answer 2: {len(sizes_needed - sizes_avail) >= 0}")

print(f"Answer 3: {sizes_needed in sizes_avail}")

print(f"Answer 4: {sizes_needed.union(sizes_avail)}")
