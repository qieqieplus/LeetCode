func removeElement(nums []int, val int) int {
	i, j := 0, len(nums)-1
	for {
		for {
			if i > j {
				return i
			}
			if nums[i] != val {
				i++
			} else {
				break
			}
		}

		for {
			if i > j {
				return i
			}
			if nums[j] == val {
				j--
			} else {
				break
			}
		}
		nums[i], nums[j] = nums[j], nums[i]
	}
}
