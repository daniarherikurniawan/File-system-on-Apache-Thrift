namespace java file_system_viewer
namespace py file_system_viewer

typedef i32 int // We can use typedef to get pretty names for the types we are using
service FileSystemService
{
        string DIR(1:string path),
        string CREATEDIR(1:string path, 2:string nama_dir),
        string GETFILE(1:string path, 2:string nama_file, 3:string path_lokal),
        string PUTFILE(1:string path, 2:string nama_file, 3:string path_lokal),
}
