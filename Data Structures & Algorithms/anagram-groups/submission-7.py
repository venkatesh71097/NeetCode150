class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force...
        # groups = [] 
        # for s in strs:
        #     counts = {}
        #     for ch in s:
        #         counts[ch] = counts.get(ch, 0) + 1
        #     found = False
        #     for group_dict, word_list in groups: 
        #         if counts == group_dict:
        #             found = True
        #             word_list.append(s)
        #             break

        #     if not found:
        #         groups.append((counts, [s]))
        # res = []
        # for _, word_list in groups:
        #     res.append(word_list)
        # return res

        # from collections import defaultdict
        # groups = defaultdict(list)
        # Without defaultdict...
        # Can't have dict / mutable keys in a dict, so use tuple which is immutable

        groups = {}
        for s in strs:
            # If alphabets...
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())

        # Without ord() function... - helps for non-alphabets
        # Step 1: Get the count dict...
        #     counts = {}
        #     for ch in s:
        #         if ch not in counts:
        #             counts[ch] = 1
        #         else:
        #             counts[ch] += 1
        # Step 2: Get the unique characters and sort the unique chars...
        #     unique_chars = [ch for ch in counts]

        #     # Sorting... (Insertion sorting...)

        #     for i in range(1, len(unique_chars)):
        #         ch = unique_chars[i]
        #         j = i - 1
        #         while j >= 0 and unique_chars[j] > ch:
        #             unique_chars[j+1] = unique_chars[j]
        #             j = j - 1
        #         unique_chars[j+1] = ch
        # Step 3: We need to know the char and its frequency and have it as a tuple key
        # as anagrams are not only unique chars, but also its freq.! 
        #     signature_list = []
        #     for ch in unique_chars:
        #         signature_list.append((ch, counts[ch]))
            
        #     signature_tuple = tuple(signature_list)
        #     if signature_tuple not in groups:
        #         groups[signature_tuple] = []
            
        #     groups[signature_tuple].append(s)
        
        # # res = []
        # # for key in groups:
        # #     res.append(groups[key])
        # return list(groups.values())
