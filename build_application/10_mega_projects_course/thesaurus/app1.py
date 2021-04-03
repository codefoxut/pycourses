import json
import pathlib
from difflib import get_close_matches


class Thesaurus:
    MATCHING_CUTOFF = 0.5
    _data = None
    _unmatched_resp = "The word does not exist. Please double check it."

    def get_json_data(self):
        if self._data is None:
            _file = pathlib.Path(__file__)
            _path = pathlib.Path(_file.parent, 'data.json')
            self._data = json.load(open(_path.name))
        return self._data

    def get_best_match(self, word):
        _data = self.get_json_data()
        _match = get_close_matches(word, _data.keys(), cutoff=self.MATCHING_CUTOFF)
        resp = self._unmatched_resp
        if _match:
            if len(_match) == 1:
                resp = self._get_one_match(_match[0])
            elif len(_match) > 1:
                resp = self._handle_multiple_match(_match)
        return resp

    def _handle_multiple_match(self, _match):
        print("user input matches with these inputs.")
        for i, j in enumerate(_match):
            print(f'{i}: {j}')
        _umatch = input("choose one to get definition! ")
        _dat = int(_umatch.strip())
        if _dat <= len(_umatch):
            word = _match[_dat]
            resp = self.define(word)
        else:
            resp = "The wrong input has been selected."
        return resp

    def _get_one_match(self, _word):
        resp = self._unmatched_resp
        yn = input(f"Did you mean {_word} instead? Enter Y if yes, or N if no.")
        if yn.upper() == 'Y':
            resp = self.define(_word)
        elif yn.upper() != 'N':
            resp = "The wrong input has been selected."
        return resp

    def define(self, word):
        word = word.strip()
        _data = self.get_json_data()
        if word in _data:
            resp = _data[word]
        elif word.lower() in _data:
            resp = _data[word.lower()]
        elif word.upper() in _data:
            resp = _data[word.upper()]
        elif word.title in _data:
            resp = _data[word.title()]
        else:
            resp = self.get_best_match(word)

        if isinstance(resp, list):
            resp = "\n".join([f'-> {i}' for i in resp])
        return resp

    def run(self):
        x = True
        while x:
            _word = input("Enter a word: ")
            print(self.define(_word))
            x = bool(_word.strip())


if __name__ == "__main__":
    t = Thesaurus()
    t.run()
