def prb(self, smth):
    ans = initial
    l = 0

    for r in range(len(smth)):

        # include smth[r] into window
        # (e.g., total += smth[r], or count[smth[r]] += 1)

        while bad_condition:
            # remove smth[l] from window
            # (e.g., total -= smth[l], or count[smth[l]] -= 1)
            l += 1

        # now window is valid
        ans = update(ans)

    return ans