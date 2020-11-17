from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UClt1tI-yikfgOfCmTT0B6SA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
        }
    # 将步骤设计为字典，然后用for循环执行
    steps = [
        GetVideoList(),
        ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
