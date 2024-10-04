from convert_image import run as convert_run
from compress_image import run as compress_run
import inquirer

def main():
    # 首先询问用户是否进行图片转换或压缩
    questions = [
        inquirer.List(
            'operation',
            message="What would you like to do?",
            choices=['Convert Image', 'Compress Image', 'Exit'],
        )
    ]

    answers = inquirer.prompt(questions)

    if answers['operation'] == 'Convert Image':
        # 如果选择了图片转换，进一步询问是否需要压缩
        compress_question = [
            inquirer.Confirm(
                'compress',
                message="Would you like to compress the image after converting?",
                default=False
            )
        ]
        compress_answer = inquirer.prompt(compress_question)

        # 执行转换操作
        convert_run()

        # 根据用户选择，决定是否执行压缩操作
        if compress_answer['compress']:
            compress_run(True)

    elif answers['operation'] == 'Compress Image':
        # 只进行压缩操作
        compress_run(False)

    else:
        print("Exiting...")

if __name__ == '__main__':
    main()