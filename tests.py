import unittest
import MarkovText

class TestMarkov(unittest.TestCase):
    def test_generate(self):
        m = MarkovText.Markov()
        t = "word word word word word word word."
        m.generate_word_dict(t)
        self.assertEqual(m.word_dict[("word.",)][''], 1.0)
        self.assertAlmostEqual(m.word_dict[("word",)]['word'], 0.8333333333)
        self.assertAlmostEqual(m.word_dict[("word",)]['word.'], 1-0.8333333333)

    def test_generate_diff(self):
        m = MarkovText.Markov()
        t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse tortor nibh, ornare id malesuada in, iaculis et neque. Donec at finibus metus."
        m.generate_word_dict(t)
        self.assertEqual(m.word_dict[("Lorem",)]['ipsum'], 1.0)
        self.assertEqual(m.word_dict[("Lorem","ipsum")]['dolor'], 1.0)
        self.assertEqual(m.word_dict[("Donec","at")]['finibus'], 1.0)

    def test_next(self):
        m = MarkovText.Markov()
        t = "word word word word word word word."
        m.generate_word_dict(t)
        self.assertEqual(m.next_word(("word.",)),"")

    def test_next_diff(self):
        m = MarkovText.Markov()
        t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse tortor nibh, ornare id malesuada in, iaculis et neque. Donec at finibus metus."
        m.generate_word_dict(t)
        self.assertEqual(m.next_word(("Lorem",)), "ipsum")
        self.assertEqual(m.next_word(("ornare",)), "id")

if __name__ == "__main__":
    unittest.main()
