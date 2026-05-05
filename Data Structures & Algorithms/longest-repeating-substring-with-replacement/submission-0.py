class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def getMaxFreq(all_freq: {}):
            m_freq = 0
            for a, f in a_f.items():
                m_freq = max(m_freq, f)
            return m_freq

        l, max_length, a_f, c_m_f = 0, 0, {}, 0

        for idx, ch in enumerate(s):
            a_f[ch] = a_f[ch]+1 if ch in a_f else 1
            while idx-l+1 - getMaxFreq(a_f) >k:
                remove_ch = s[l]
                a_f[remove_ch] -= 1
                l += 1
            print(s[l:idx])
            max_length = max(max_length, idx-l+1)
        
        return max_length
                


        