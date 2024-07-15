class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        create a dictionary that keep track of the counts from chars
        we can iterate through check if each char is in the str in the words array
        have a coutner that adds the len of each of the strings
        '''
        char_dict = {}
        for char in chars:
            char_dict[char] = char_dict.get(char,0) + 1
        
        ans = 0
        for word in words:
            broken = False
            for char in word:
                if char not in char_dict or word.count(char) > char_dict[char] :
                    broken = True
                    break

            if broken == False:
                ans += len(word)

        return ans
            
