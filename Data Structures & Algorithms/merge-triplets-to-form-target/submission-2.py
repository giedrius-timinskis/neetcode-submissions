class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_x, found_y, found_z = False, False, False
        for x, y, z in triplets:
            tar_x, tar_y, tar_z = target[0], target[1], target[2]
            # Make sure neither of the triplet values exceed the target at that index
            # Satisfies the example provided: 'if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2]'
            if x <= tar_x and y <= tar_y and z <= tar_z:
                # If any of the indices of the triplet match the target, it means we found the max val
                if x == tar_x:
                    found_x = True
                if y == tar_y:
                    found_y = True
                if z == tar_z:
                    found_z = True

        return found_x and found_y and found_z