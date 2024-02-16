import git

def update_from_git(repo_path, local_path):
    # Проверяем наличие папки для репозитория
    if not os.path.exists(local_path):
        # Если папки нет, клонируем репозиторий
        repo = git.Repo.clone_from(repo_path, local_path)
    else:
        # Если папка уже существует, просто обновляем ее
        repo = git.Repo(local_path)
        origin = repo.remote('origin')
        origin.fetch()
        if repo.is_dirty():
            # Ваши действия при обнаружении изменений, например, загрузка новой версии файла
            origin.pull()
