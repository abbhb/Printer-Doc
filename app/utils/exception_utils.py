# -*- coding: utf-8 -*-
import traceback


class ExceptionUtils:
    @classmethod
    def exception_traceback(cls, e):
        # 打印异常的堆栈跟踪信息
        print(f"\nException: {str(e)}\nCallstack:\n{traceback.format_exc()}\n")


if __name__ == '__main__':
    try:
        raise Exception('exception test')
    except Exception as e:
        ExceptionUtils.exception_traceback(e)
