import sys

from wordcloud import WordCloud


class WordCloudGenerator:
    def __init__(self, file_path: str):
        with open(file_path) as f:
            self.text = f.read()

    def __call__(self, output_path: str, **kwargs) -> None:
        """
        Generate a word cloud image.

        :param output_path: The path to the output file.
        """
        WordCloud(**kwargs).generate(self.text).to_file(output_path)


if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    wordcloud_obj = WordCloudGenerator(input_path)
    wordcloud_obj(
        output_path,
        width=1920,
        height=1080,
        background_color='black',
        colormap='gray',
    )
