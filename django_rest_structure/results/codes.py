class ResultMessageStructure:
    def __init__(self, code: int, message: str, is_success_result: bool):
        self.code, self.message, self.is_success_result = code, message, is_success_result


class ResultMessages:
    GET_SUCCESSFULLY = ResultMessageStructure(200, 'Done', True)
    SUBMIT_SUCCESSFULLY = ResultMessageStructure(201, 'Submit', True)
    PAGE_NOT_FOUND = ResultMessageStructure(404, 'Page Not Found', False)
    UNDEFINED_ERROR = ResultMessageStructure(500, 'Undefined Error.', False)
    ENTERED_DATA_NOT_VALID = ResultMessageStructure(406, 'Entered Data Is Not Valid', False)
    UNDEFINED_METHOD = ResultMessageStructure(405, 'Invalid Method', False)
    INVALID_CONTENT_TYPE = ResultMessageStructure(405, 'Entered Content-Type Is Not Valid', False)
    AUTHENTICATION_FAIL = ResultMessageStructure(403, 'Unauthorized', False)
    HTTP_ERROR_404 = ResultMessageStructure(-404, '404 Error', False)
    HTTP_ERROR_400 = ResultMessageStructure(-400, '400 Error', False)
    HTTP_ERROR_403 = ResultMessageStructure(-403, '403 Error', False)
    HTTP_ERROR_500 = ResultMessageStructure(-500, '500 Error', False)
