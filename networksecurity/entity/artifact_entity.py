from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str



@dataclass
class DataValidationArtifact:
    def __init__(
        self,
        validation_status: bool,
        valid_train_file_path: str,
        valid_test_file_path: str,
        invalid_train_file_path: str,
        invalid_test_file_path: str,
        drift_report_file_path: str
    ):
        self.validation_status = validation_status
        self.valid_train_file_path = valid_train_file_path
        self.valid_test_file_path = valid_test_file_path
        self.invalid_train_file_path = invalid_train_file_path
        self.invalid_test_file_path = invalid_test_file_path
        self.drift_report_file_path = drift_report_file_path   