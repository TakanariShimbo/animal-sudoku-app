from typing import Literal


class Texts:
    def __init__(self, lang: Literal["jp", "en"]) -> None:
        self._lang = lang

    @property
    def is_jp(self) -> bool:
        return self._lang == "jp"

    @property
    def is_en(self) -> bool:
        return self._lang == "en"

    @property
    def column_header(self) -> str:
        if self.is_jp:
            return "列"
        elif self.is_en:
            return "C"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def index_header(self) -> str:
        if self.is_jp:
            return "行"
        elif self.is_en:
            return "R"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def title(self) -> str:
        if self.is_jp:
            return "🐧アニマル数独アプリ"
        elif self.is_en:
            return "🐧Animal Sudoku App"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def change_lang(self) -> str:
        if self.is_jp:
            return "🗾言語切替"
        elif self.is_en:
            return "🗽Language"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def change_problem(self) -> str:
        if self.is_jp:
            return "🐸問題を変える"
        elif self.is_en:
            return "🐸Change"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def number_of_empty_cells(self) -> str:
        if self.is_jp:
            return "空白なマスの数"
        elif self.is_en:
            return "Number of empty cells"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def change(self) -> str:
        if self.is_jp:
            return "変更"
        elif self.is_en:
            return "Change"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def explanation(self) -> str:
        if self.is_jp:
            return "🐔説明を見る"
        elif self.is_en:
            return "🐔Explanation"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def restart(self) -> str:
        if self.is_jp:
            return "🐶最初から"
        elif self.is_en:
            return "🐶Restart"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def answer(self) -> str:
        if self.is_jp:
            return "🐗回答を見る"
        elif self.is_en:
            return "🐗Answer"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def explanation_contents(self) -> str:
        if self.is_jp:
            return "🐧縦一列・横一列・3x3グリッド に同じ動物（数字）が入らないようにしてね"
        elif self.is_en:
            return "🐧Make sure the same animal (number) does not appear in a single column, row, or 3x3 grid"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def example_vertical(self) -> str:
        if self.is_jp:
            return "⚠️縦一列の例"
        elif self.is_en:
            return "⚠️Example of a single row"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def example_horizontal(self) -> str:
        if self.is_jp:
            return "⚠️横一列の例"
        elif self.is_en:
            return "⚠️Example of a single column"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def example_grid(self) -> str:
        if self.is_jp:
            return "⚠️3x3グリッドの例"
        elif self.is_en:
            return "⚠️Example of a 3x3 grid"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def not_empty_alert(self) -> str:
        if self.is_jp:
            return "🐧埋まっているマスは変えられないよ"
        elif self.is_en:
            return "🐧The filled cells cannot be changed"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def not_number_alert(self) -> str:
        if self.is_jp:
            return "🐧1から9の数字を入力してね"
        elif self.is_en:
            return "🐧Enter numbers from 1 to 9"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def can_not_solve_alert(self) -> str:
        if self.is_jp:
            return "🐧その数字は入れられないよ"
        elif self.is_en:
            return "🐧That number cannot be entered"
        raise Exception("lang at Texts should be 'ja' or 'en'!")

    @property
    def thanks(self) -> str:
        if self.is_jp:
            return "🐧遊んでくれてありがとう"
        elif self.is_en:
            return "🐧Thank you for playing"
        raise Exception("lang at Texts should be 'ja' or 'en'!")
