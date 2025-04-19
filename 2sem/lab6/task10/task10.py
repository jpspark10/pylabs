import argparse
import textwrap


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        return str(e)
    wrapper = textwrap.TextWrapper(width=frame_width, replace_whitespace=False)
    lines = []
    for paragraph in text.splitlines():
        lines.extend(wrapper.wrap(paragraph) or [''])
        if len(lines) >= frame_height:
            break
    return "\n".join(lines[:frame_height])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int, required=True)
    parser.add_argument('--frame-width', type=int, required=True)
    parser.add_argument('file_name')
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.file_name))
