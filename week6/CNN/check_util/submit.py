from pathlib import Path
import platform
import shutil
import os
import zipfile

def process_submit():
    plat_system = platform.system()
    # 프로젝트 디렉토리 설정
    project_path = Path().cwd().absolute()

    # 제출 파일 설정
    file_name = "(중급) 29차시_프로젝트 9 제출코드(CNN).ipynb"
    submit_file = project_path / file_name  # 직접 파일 경로 설정

    # 평가 기준 파일 설정 (분할 없이 직접 지정)
    submit_rubric_file = Path("/Users/juwonkim/Desktop/네이버 부스트코스 AI 엔지니어/week66/02_cnn_pt/check_util/cnn_submission.tsv")

    # 제출 파일 저장 디렉토리
    output_path = project_path / "submit"
    if not output_path.exists():
        output_path.mkdir()

    print(f"[ Self-Check ] 시스템: {plat_system}")
    
    # checking all pass or not
    x = submit_rubric_file.read_text(encoding="utf-8").splitlines()[1:]
    # remove blank first & end point
    x = [line.strip() for line in x]
    check_func = lambda x: True if x == "Pass" else False
    check_list = []
    for i, line in enumerate(x, 1):
        temp = line.split("\t")
        if check_func(temp[-1]):
            check_list.append(1)
        else:
            check_list.append(0)
            print("""[ Self-Check ] 
            [평가기준-{}] 통과하지 못했습니다. 다음 항목을 참고하세요!
            항목: '{}', 
            기준: '{}', 
            세부기준: '{}'""".format(i, *temp[:-1]))
    if sum(check_list) == len(x):
        # 제출 파일 생성
        shutil.copy(str(submit_rubric_file), str(output_path))
        # sub_string = f"jupyter nbconvert --to html --output {file_name.split('-')[1]}_submission --output-dir={str(output_path)} '{str(submit_file)}'"
        # os.system(sub_string)
        # print(f"[ Self-Check ] Submit 파일 생성완료! 위치: '{output_path.relative_to(project_path)}'")
        sub_string = f"jupyter nbconvert --to html --output submission.html --output-dir={str(output_path)} '{str(submit_file)}'"
        os.system(sub_string)
        
        print(f"[ Self-Check ] Submit 파일 생성완료! 위치: '{output_path.relative_to(project_path)}'")
        

        # 압축 파일 생성
        with zipfile.ZipFile(project_path / "submit.zip", "w", zipfile.ZIP_DEFLATED) as zip_handle:
            for f in output_path.glob("*submission.*"):
                zip_handle.write(f, arcname=f.relative_to(project_path))
        print("[ Self-Check ] submit.zip 생성 완료!")
        print("[ Self-Check ] 모든 평가기준을 통과했습니다. 압축파일을 제출해주세요!")
    else:
        print("[ Self-Check ] 일부 평가기준을 통과하지 못했습니다. 제출 파일이 생성되지 않습니다. 다시 시도해보세요!")