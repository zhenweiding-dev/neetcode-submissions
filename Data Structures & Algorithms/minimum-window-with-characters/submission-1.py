class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        i 2strs, s t
        o shortest substring of s, that contains every char in t, including duplicates; or ""
        c correct ouput is unique(not many, only first); len(s)&len(t) in [1, 1000]; s, t contains upper and lowercase
        e len(s) < len(t); t = ""

        use dict to store char freq in t

        use a sliding window to check if char freq in window is equal or larger than t
        if all g or e, return substr in the window, else return ""
        
        to check, use have & need to updated check result
        """
        len_s, len_t = len(s), len(t)

        if not t or len_s < len_t:
            return ""
        
        dict_t, window = {}, {}
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        
        need = len(dict_t)
        l, have = 0, 0

        # use lst and lstlen to track shortest substr
        res, len_res = [-1, -1], len_s + 1

        for r in range(len_s):
            #update window
            c = s[r]
            window[c] = window.get(c, 0) + 1

            #update have
            if c in dict_t and window[c] == dict_t[c]:
                have += 1
            
            while have == need:
                # check and undate result
                # check if find shorter res
                if r - l + 1 < len_res:
                    res = [l, r]
                    len_res = r - l + 1
                
                # check and update left to find even shorter res
                c = s[l]
                window[c] -= 1

                #check if 'have' changed
                if c in dict_t and window[c] < dict_t[c]:
                    have -= 1 # end loop and update right to find a new res
                l += 1
        l, r = res
        return s[l : r + 1] if len_res <= len_s else ""





        
