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
    public partial class MainFormBean : Form
    {
        //각 버튼의 클릭 값, 날짜를 세는 변수
        int day = 0;
        int waterCount = 0, gameCount = 0, drawCount = 0, codingCount = 0;
        //파일 저장, 불러오기에 사용되는 객체 생성
        OpenFileDialog openFileDialog1 = new OpenFileDialog();
        SaveFileDialog saveFileDialog1 = new SaveFileDialog();
        //배경가져오기Form에 사용될 변수
        Bitmap bmp;

        public MainFormBean()
        {
            InitializeComponent();

            this.day = 0;
            this.waterCount = 0;
            this.gameCount = 0;
            this.drawCount = 0;
            this.codingCount = 0;
            
        }

        //Paint에서 그린 이미지 저장하여 PictureBox에 나타나게함

        //각 버튼은 5일 전 후로 안내창이 다르다.
        //콩에게 물을준다(메세지창)
        private void btnWater_Click(object sender, EventArgs e)
        {
            if( day == 5)
            {
                MessageBox.Show("콩은 다 자랐습니다! 콩과 작별해주세요","안녕콩",MessageBoxButtons.OK);
            }else
            {
                MessageBox.Show("콩은 물을 맛있게 마셨다","콩에게 물주기",MessageBoxButtons.OK);
                waterCount++;
                day++;
                lblDay.Text = "Day "+day;
                ProBarDay.Value = day;
            }

        }

        //과일경주 폼을 실행시킨다
        private void btnGame_Click(object sender, EventArgs e)
        {
            if (day == 5)
            {
                MessageBox.Show("콩은 다 자랐습니다! 콩과 작별해주세요", "안녕콩", MessageBoxButtons.OK);
            }
            else
            {
                
                gameCount++;
                day++;
                lblDay.Text = "Day " + day;
                ProBarDay.Value = day;

                GameForm obj = new GameForm();

                obj.ShowDialog();
                //경기 결과를 StatusBar에 표시한다
                toolbl.Text = obj.Msg;
            }
        }

        //그림판 폼을 실행시킨다(X)
        //배경을 성정하는 폼을 실행시킨다.
        private void btnDraw_Click(object sender, EventArgs e)
        {
            if (day == 5)
            {
                MessageBox.Show("콩은 다 자랐습니다! 콩과 작별해주세요", "안녕콩", MessageBoxButtons.OK);
            }
            else
            {
                drawCount++;
                day++;
                lblDay.Text = "Day " + day;
                ProBarDay.Value = day;

                PaintNewForm obj = new PaintNewForm();
                obj.ShowDialog();

                bmp = new Bitmap(obj.ImgName);
                picBoxBorrow.Image = bmp;
            }
        }

        //코딩 : 메세지창에서 입력받은 말을 Status에 뜨게 한다
        private void btnCoding_Click(object sender, EventArgs e)
        {
            if (day == 5)
            {
                MessageBox.Show("콩은 다 자랐습니다! 콩과 작별해주세요", "안녕콩", MessageBoxButtons.OK);
            }
            else
            {
                codingCount++;
                day++;
                lblDay.Text = "Day " + day;
                ProBarDay.Value = day;

                CodeInMainForm obj = new CodeInMainForm();
                obj.ShowDialog();
                toolbl.Text = obj.Sendmessage;
            }
        }

        //새로키우기 버튼을 눌렀을 경우 모든 값 초기화
        private void 새로키우기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            day = 0;
            waterCount = 0;
            gameCount = 0;
            drawCount = 0;
            codingCount = 0;

            //시각적인 정보를 바꿔준다
            ProBarDay.Value = waterCount;
            lblDay.Text = "Day " + day;

            MessageBox.Show("정보가 초기화 되었습니다", "새로키우기", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
        }

        //ToolBox에 대한 명령은 MenuBox에서 지정한 명령을 사용한다
        //불러오기
        private void 열기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            btnOpen_Click(sender, e);
        }

        //저장
        private void 저장ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            btnSave_Click(sender, e);
        }

        //끝
        private void 종료ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }

        //txt파일 형식으로 변수들 정보를 저장한다
        private void btnSave_Click(object sender, EventArgs e)
        {
            saveFileDialog1.InitialDirectory = @"C:\";
            saveFileDialog1.Filter = "텍스트파일(*.txt)|*.txt|모든파일(*.*)|*.*";
            saveFileDialog1.FilterIndex = 1;
            saveFileDialog1.RestoreDirectory = true;

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                MySave(saveFileDialog1.FileName);
            }
        }

        //필드값 정보를 txt형식으로 저장
        private void MySave(string s)
        {
            string str = day + "/" + waterCount + "/" + gameCount + "/" + drawCount + "/" + codingCount;

            StreamWriter sw = File.CreateText(s); //파일의 스트림은 연다
            sw.WriteLine(str);//txtBox의 내용을 파일로 기록
            sw.Close(); //열었던 스트림을 닫는다
        }

        //txt파일 형식으로 저장된 내용을 풀어 본문에 적용한다
        private void btnOpen_Click(object sender, EventArgs e)
        {
            //open창을 꾸민다
            openFileDialog1.InitialDirectory = @"C:\";
            openFileDialog1.Filter = "텍스트파일(*.txt)|*.txt|모든파일(*.*)|*.*";
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.Multiselect = true;

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                MyOpen(openFileDialog1.FileName);
            }
        }

        //txt파일에 저장된 형식을 MainForm필드에 적용
        private void MyOpen(string s)
        {
            string digit = "";
            StreamReader sr = File.OpenText(s); //파일의스트림을 연다
            digit = sr.ReadToEnd(); //파일의 내용을 txtBox에 출력
            string[] str = digit.Split('/');

            //값을 int형으로 바꾸고 초기화
            this.day = Convert.ToInt32(str[0]);
            this.waterCount = Convert.ToInt32(str[1]);
            this.gameCount = Convert.ToInt32(str[2]);
            this.drawCount = Convert.ToInt32(str[3]);
            this.codingCount = Convert.ToInt32(str[4]);

            sr.Close();

            //시각적인 정보를 바꿔준다
            ProBarDay.Value = waterCount;
            lblDay.Text = "Day " + day;
        }

        //엔딩(6일차)전엔 아직 엔딩을 볼 수 없음 메세지창, 엔딩Form
        private void btnEnd_Click(object sender, EventArgs e)
        {
            //5일 전 엔딩을 볼 수 없다
            if( day == 5)
            {
                //값을 전달하는 Contain클래스를 만들어 전달(질문 전 방식)
                Contain c = new Contain(waterCount, gameCount, drawCount, codingCount);

                EndForm end = new EndForm(c);
                end.ShowDialog();

                //종료한 EndForm에서 값을 전달받음
                day = end.Day;
                waterCount = end.WaterCount;
                gameCount = end.GameCount;
                drawCount = end.DrawCount;
                codingCount = end.CodingCount;

                ProBarDay.Value = waterCount;
                lblDay.Text = "Day " + day;
            }
            else
            {
                MessageBox.Show("아직 콩은 자라고 있습니다. \nDay5가 되면 엔딩을 볼 수 있습니다.","자라는콩",MessageBoxButtons.OK);
            }
        }
    }//mainform end

    //subForm에 값을 전달하기 위한 클래스(질문 전 방법)
    public class Contain
    {
        int waterCount = 0, gameCount = 0, drawCount = 0, codingCount = 0;

        public Contain() { }

        public Contain(int waterCount, int gameCount, int drawCount, int codingCount)
        {
            this.waterCount = waterCount;
            this.gameCount = gameCount;
            this.drawCount = drawCount;
            this.codingCount = codingCount;
        }

        public int WaterCount
        {
            get { return waterCount; }
        }
        public int GameCount
        {
            get { return gameCount; }
        }
        public int DrawCount
        {
            get { return drawCount; }
        }
        public int CodingCount
        {
            get { return codingCount; }
        }
       
    }
}
