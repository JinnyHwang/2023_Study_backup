using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BringUpBean
{
    public partial class EndForm : Form
    {
        //전달받은 값을 저장하기 위한 변수
        int waterCount = 0, gameCount = 0, drawCount = 0, codingCount = 0;
        int day = 0;
        string result = "result";

        public EndForm()
        {
            InitializeComponent();
        }

        public EndForm(Contain c)
        {
            InitializeComponent();

            //생성될 때 저장받은 값으로 result에 저장
            this.waterCount = c.WaterCount;
            this.gameCount = c.GameCount;
            this.drawCount = c.DrawCount;
            this.codingCount = c.CodingCount;

            if (waterCount >= 4) //4번이상 물을 준 경우
            {
                result = "Big";

            }else if (gameCount >= 3) //3번이상 게임을 한 경우
            {
                result = "Progamer";

            }else if (codingCount >= 3) //3번이상 코딩을 한 경우
            {
                result = "Programmer";

            }else if(drawCount >= 3) //3번이상 배경가져오기(그리기)를 한 경우
            {
                result = "Painter";

            }else //아무것도 아닐 때
            {
                result = "Plain";
            }



        }

        //새로시작하기 버튼을 누를 경우
        private void btnNewBean_Click(object sender, EventArgs e)
        {
            //초기화시킨 값을 MainForm에 전달
            MainFormBean obj = new MainFormBean();
            waterCount = 0; gameCount = 0; drawCount = 0; codingCount = 0;
            Close();
        }

        //엔딩에따라 다른 이미지를 나타내기
        private void EndForm_Load(object sender, EventArgs e)
        {
            if (result == "Plain")
            {
                lblFinalBean.Text = "행복한 평범콩";
                picBoxEnd.Image = imgListBeanEnding.Images[0];

            }else if (result == "Big")
            {
                lblFinalBean.Text = "통통콩";
                picBoxEnd.Image = imgListBeanEnding.Images[1];

            }
            else if (result == "Progamer")
            {
                lblFinalBean.Text = "프로게이머콩";
                picBoxEnd.Image = imgListBeanEnding.Images[3];

            }
            else if (result == "Programmer")
            {
                lblFinalBean.Text = "공돌이콩";
                picBoxEnd.Image = imgListBeanEnding.Images[4];

            }
            else if (result == "Painter")
            {
                lblFinalBean.Text = "예술가콩";
                picBoxEnd.Image = imgListBeanEnding.Images[2];

            }

        }
        //waterCount = 0, gameCount = 0, drawCount = 0, codingCount = 0;

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
        public int Day
        {
            get { return day; }
        }
    }
}
