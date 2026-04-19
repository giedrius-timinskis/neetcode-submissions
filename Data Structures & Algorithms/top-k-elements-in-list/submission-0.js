class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
          const results = {};
    const valuesArr = Array.from({ length: nums.length }, () => []);

    for (let i = 0; i < nums.length; i++) {
        const no = nums[i];

        if (!results[no]) {
            results[no] = 1;
            valuesArr[0].push(no);
            continue;
        } else {
            const previousNo = results[no] - 1;
            results[no]++;

            valuesArr[previousNo] = valuesArr[previousNo].filter(
                (val) => val !== no,
            );
            valuesArr[previousNo + 1].push(no);
        }
    }

    const result = [];

    for (let i = valuesArr.length - 1; i >= 0; i--) {
        const vals = valuesArr[i];

        if (vals.length === 0) continue;

        for (let j = 0; j < vals.length; j++) {
            result.push(vals[j]);
            if (result.length === k) return result;
        }
    }

    return result;
    }
}