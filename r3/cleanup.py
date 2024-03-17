import os

def delete_files_with_extensions(extensions):
    """Deletes all files with the specified extensions in the directory where the script is located.
    
    Parameters
    ----------
    :param extensions: A list of extensions of files to delete
    :type extensions: list
    :return: None
    :rtype: None
    
    .. versionadded:: 1.0.0
    """
    
    # Get the directory where the script is located
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # List all files in the directory
    files_in_directory = os.listdir(dir_path)

    # Filter files by the specified extensions
    files_to_delete = [file for file in files_in_directory if file.endswith(tuple(extensions))]

    # Ask for user confirmation
    print("The following files will be deleted:")
    for file in files_to_delete:
        print(file)
    response = input("Are you sure you want to proceed? (y/n): ")

    # Check user response
    if response.lower() == 'y':
        # Delete the files
        for file in files_to_delete:
            os.remove(os.path.join(dir_path, file))
            print(f"Deleted: {file}")
        print("Deletion complete.")
    else:
        print("Deletion canceled.")
        
# Specify the extensions of files you want to delete
extensions_to_delete = ['.aux', '.lof', '.log', '.lot', '.fls', '.out', '.toc', '.fmt', '.fot', '.cb', '.cb2', '.lb', '.dvi', '.xdv', '-converted-to.', '.bbl', '.bcf', '.blg', '-blx.aux', '-blx.bib', '.run.xml', '.fdb_latexmk', '.synctex', '.synctex(busy)', '.synctex.gz', '.synctex.gz(busy)', '.pdfsync', '.alg', '.loa', '.idx', '.ilg', '.ind']

if __name__ == "__main__":
    # Call the function
    delete_files_with_extensions(extensions_to_delete)