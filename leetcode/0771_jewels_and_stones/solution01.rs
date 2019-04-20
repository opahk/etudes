use std::collections::HashMap;

impl Solution {
    pub fn num_jewels_in_stones(j: String, s: String) -> i32 {
        let mut count = 0;
        let mut cache = HashMap::new();
        for i in j.chars() {
            cache.insert(i, 1);
        }
        for l in s.chars() {
            if cache.contains_key(&l) {
                count += 1;
            }
        }
        return count;
    }
}
