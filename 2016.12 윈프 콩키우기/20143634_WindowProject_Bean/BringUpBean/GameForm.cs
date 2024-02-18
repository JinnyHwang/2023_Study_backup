using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

namespace BringUpBean
{
    
    public partial class GameForm : Form
    {
        int btncount = 0;
        private Fruit[] fruits;
        private Random randG;
        //SimpleThread tobj = new SimpleThread();
        string msg = null;

        public string Msg
        {
            get { return msg; }
        }
        public GameForm()
        {
            InitializeComponent();
        }



        //스레드사용 경주게임 시작
        private void btnGameStart_Click(object sender, EventArgs e)
        {
            btncount++;

            //ThreadStart ts = new ThreadStart(tobj.ThreadBody);
            //Thread t = new Thread(ts);

            //다음날이 되어도 같을 결과가 되지 않도록 메소드 안에서 객체 생성
            fruits = new Fruit[3];
            randG = new Random();

            // 시작 위치는 28, 개의 길이는 75, 트랙의 길이는 450(PictureBox의 Length가 아니라 직접 잼)
            fruits[0] = new Fruit() { FruitImg = picBerry, StartPoint = 200, LengthTrack = 300, Randomizer = randG };
            fruits[1] = new Fruit() { FruitImg = picPeach, StartPoint = 200, LengthTrack = 300, Randomizer = randG };
            fruits[2] = new Fruit() { FruitImg = picApple, StartPoint = 200, LengthTrack = 300, Randomizer = randG };

            bool win = false;
            int winFruit = -1;

            //아무것도 선택하지 않으면 안내창이 뜬다.
            if (raBtnApple.Checked == false && raBtnBerry.Checked == false && raBtnPeach.Checked == false)
            {
                MessageBox.Show("과일을 선택해 주세요", "안내", MessageBoxButtons.OK);
            }
            else
            {//선택 시 경기시작
                while (win != true)
                {
                    for (int i = 0; i < 3 && win == false; i++) //승자가 아직 안날 경우 계속 반복한다
                    {
                        win = fruits[i].StartRun();
                        if (win == true)
                        {
                            winFruit = i;
                        }
                    }
                    //t.Start();
                    //Thread.Sleep(10);
                    System.Threading.Thread.Sleep(10);
                }

                //승자 == radioBtn : 이겼다!
                if (winFruit == 0 && raBtnBerry.Checked == true)
                {
                    msg = "축하합니다! 딸기가 이겼습니다!";
                    //MessageBox.Show(msg, "Win", MessageBoxButtons.OK);
                }
                else if (winFruit == 1 && raBtnPeach.Checked == true)
                {
                    msg = "축하합니다! 복숭아가 이겼습니다!";
                    //MessageBox.Show(mag, "Win", MessageBoxButtons.OK);
                }
                else if (winFruit == 2 && raBtnApple.Checked == true)
                {
                    msg = "축하합니다! 사과가 이겼습니다!";
                    //MessageBox.Show("축하합니다! 사과가 이겼습니다!", "Win", MessageBoxButtons.OK);
                }
                else
                {
                    msg = "아쉽네요 다음날에 다시 도전해보세요!";
                   // MessageBox.Show("아쉽네요 다음날에 다시 도전해보세요!", "Lose", MessageBoxButtons.OK);
                }
                MessageBox.Show(msg, "Win", MessageBoxButtons.OK);
            }
            
        }

        //폼을 종료하고 경기결과를 이전폼에 전달한다
        private void btnGameEnd_Click(object sender, EventArgs e)
        {
            //아무것도 선택하지 않으면 안내창
            if(raBtnApple.Checked == false && raBtnBerry.Checked == false && raBtnPeach.Checked == false)
            {
                MessageBox.Show("과일을 선택해 주세요","안내",MessageBoxButtons.OK);
            }
            //경기를 시작하지 않았을 때 안내창
            else if (btncount == 0)
            {
                MessageBox.Show("경기를 시작해 주세요", "안내", MessageBoxButtons.OK);
            }
            else
            {
                Close();
            }
        }

        private void GameForm_MouseMove(object sender, MouseEventArgs e)
        {
            //좌표확인 끝
            //label1.Text = e.X + ", " + e.Y;
        }

        
    }//GameForm end

    class Fruit
    {
        //시작점, 경주트랙길이, img객체의 트랙위에서의 위치
        private int startPoint = 0, lengthTrack = 0, imgPosition = 0;
        private PictureBox fruitImg = null; //이미지객체
        public Random Randomizer = null; //랜덤함수
        
        
        public bool StartRun()
        {
            int digitRand; //랜덤함수 저장위치

            digitRand = Randomizer.Next(10) + 1; //1~10칸 랜덤 이동
            //img객체의 x좌표에 랜덤값을 넣는다
            Point p = fruitImg.Location; //좌표에 현재 img객체의 위치값 넣는다
            p.X += digitRand; //랜덤값을 X좌표에 넣어 이동시긴다
            fruitImg.Location = p; //바뀐 좌표값을 다시 객체의 좌표값에 넣어준다

            imgPosition = p.X;

            if(imgPosition >= (startPoint + lengthTrack))
            {
                return true; //도착지점에 도착해 경기가 끝남
            }
            else
            {
                return false; //아직 도착하지 않았으면 false로 반환 
            }
        }


        public int StartPoint
        {
            get { return startPoint; }
            set { this.startPoint = value; }
        }
        public int LengthTrack
        {
            get { return lengthTrack; }
            set { this.lengthTrack = value; }
        }
        public int ImgPosition
        {
            get { return imgPosition; }
            set { this.imgPosition = value; }
        }
        public PictureBox FruitImg
        {
            get { return fruitImg; }
            set { this.fruitImg = value; }
        }

    }//FruitClass end

    /*
    class SimpleThread
    {
        public void ThreadBody()
        {
            Thread.Sleep(10); 
        }
    }*/
}
