import unittest
from MarkovText import MarkovText

class TestMarkov(unittest.TestCase):
    def test_generate(self):
        m = MarkovText.Markov()
        t = "word word word word word word word."
        m.add_to_dict(t)
        t = "test word."
        m.add_to_dict(t)
        self.assertEqual(m.word_dict[("word.",)][''].prob, 1.0)
        self.assertEqual(m.word_dict[("test",)]['word.'].prob, 1.0)
        self.assertAlmostEqual(m.word_dict[("word",)]['word'].prob, 0.8333333333)
        self.assertAlmostEqual(m.word_dict[("word",)]['word.'].prob, 1-0.8333333333)

    def test_generate_diff(self):
        m = MarkovText.Markov()
        t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse tortor nibh, ornare id malesuada in, iaculis et neque. Donec at finibus metus."
        m.add_to_dict(t)
        self.assertEqual(m.word_dict[("Lorem",)]['ipsum'].prob, 1.0)
        self.assertEqual(m.word_dict[("Lorem","ipsum")]['dolor'].prob, 1.0)
        self.assertEqual(m.word_dict[("Donec","at")]['finibus'].prob, 1.0)

    def test_next(self):
        m = MarkovText.Markov()
        t = "word word word word word word word."
        m.add_to_dict(t)
        self.assertEqual(m.next_word(("word.",)),"")

    def test_next_diff(self):
        m = MarkovText.Markov()
        t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse tortor nibh, ornare id malesuada in, iaculis et neque. Donec at finibus metus."
        m.add_to_dict(t)
        self.assertEqual(m.next_word(("Lorem",)), "ipsum")
        self.assertEqual(m.next_word(("ornare",)), "id")

if __name__ == "__main__":
    unittest.main()
