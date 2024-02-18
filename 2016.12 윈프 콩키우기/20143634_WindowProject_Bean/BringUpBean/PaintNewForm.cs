using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace BringUpBean
{
    public partial class PaintNewForm : Form
    {
        SaveFileDialog save;
        OpenFileDialog open;

        //파일 경로를 전달하기위한 변수
        private string imgName = "";
        Image img;
        Bitmap bmp;

        public string ImgName
        {
            get { return imgName; }
        }

        public PaintNewForm()
        {
            InitializeComponent();
            
            save = new SaveFileDialog();
            open = new OpenFileDialog();
        }

        //이미지 저장
        private void SaveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            save.Filter = "이미지파일(*.jpg)|*.jpg|이미지파일(*.png)|*.png|비트맵(*.bmp)|*.bmp";

            if(save.ShowDialog() == DialogResult.OK)
            {
                imgName = save.FileName;
                //파일 경로로 비트맵 저장
                bmp.Save(imgName);
            }
        }

        //이미지 불러오기
        private void OpenToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //처음에 C드라이브로
            open.InitialDirectory = @"C:\";
            open.Filter = "이미지파일(*.jpg)|*.jpg|이미지파일(*.png)|*.png|모든파일(*.*)|*.*";

            if(open.ShowDialog() == DialogResult.OK)
            {
                //경로저장
                imgName = open.FileName;
                //img에 저장 후 bmp에 저장
                img = Image.FromFile(imgName);
                picBox.Image = img;
                //불러온 이미지 정보로 비트맵 생성
                bmp = new Bitmap(img);
            }
        }

        //종료
        private void ExitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
