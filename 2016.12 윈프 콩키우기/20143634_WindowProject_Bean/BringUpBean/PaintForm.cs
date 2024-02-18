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
    /*
     1. Paint로 그렸을 경우 선, 사각형, 원 따로따로 출력
     2. Mouse Up, Down시 바로 선택한 도형그림을 어떻게 그려야 할지 생각하지 못하여
     마우스로 좌표를 잡고, 도형을 선택하여야 그림이 그려진다
     3. 파일저장오류 해결못함(사용한 Paint, Bitmap, Graphics에 대한 이해 부족)
         */
    public partial class PaintForm : Form
    {
        Bitmap bmp;

        int downX, downY, upX, upY;
        Point startPoint, endPoint;
        ColorDialog penColor;
        Pen drawFigure = new Pen(Color.Black);
        Graphics g;
        int count = 0;
        string checkedmenu = "";
        Rectangle r = new Rectangle(0, 0, 0, 0);

        SaveFileDialog saveFileDialog1 = new SaveFileDialog();

        public PaintForm()
        {
            InitializeComponent();

            bmp = new Bitmap(panleDraw.Width, panleDraw.Height);
        }

        //펜 굵기
        private void 굵기5ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            drawFigure.Width = 5;
        }

        private void 굵기1ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            drawFigure.Width = 1;
        }

        private void 굵기3ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            drawFigure.Width = 3;
        }

        private void 굵기10ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            drawFigure.Width = 10;
        }

        //펜 색깔
        private void 색ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            penColor = new ColorDialog();
            penColor.ShowDialog();
            drawFigure.Color = penColor.Color;

        }

        //Paint가 아닌 여기서 그림을 그릴 시 Focus를 잃으면 그림이 사라짐
        private void 선lineToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //Graphics 객체는 Paint에서 생성, 사용
            //g = panleDraw.CreateGraphics();
            //g.DrawLine(drawFigure, startPoint, endPoint);

            //체크표시 나타냄, 선택된 항목 checkedmenu변수에 이름 저장
            ToolStripMenuItem item = (ToolStripMenuItem)sender;
            foreach (ToolStripMenuItem it in item.Owner.Items)
            {
                if (it == item) //선택한 아이템에만 체크표시
                {
                    it.Checked = true; //클릭한 메뉴만 checked를 true로
                    checkedmenu = it.Name;
                }
                else
                {
                    it.Checked = false;
                }
            }

            //판넬위에 보여주기 위함
            panleDraw.Invalidate();
            panleDraw.Update();
            count++;
        }

        private void 원ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //g = panleDraw.CreateGraphics();

            //Rectangle r = new Rectangle(100, 100, 100, 100);
            //g.DrawEllipse(drawFigure, r);

            //체크표시 나타냄, 선택된 항목 checkedmenu변수에 이름 저장
            ToolStripMenuItem item = (ToolStripMenuItem)sender;
            foreach (ToolStripMenuItem it in item.Owner.Items)
            {
                if (it == item) //선택한 아이템에만 체크표시
                {
                    it.Checked = true; //클릭한 메뉴만 checked를 true로
                    checkedmenu = it.Name;
                }
                else
                {
                    it.Checked = false;
                }
            }

            //판넬위에 보여주기 위함
            panleDraw.Invalidate();
            panleDraw.Update();
            count++;
        }

        private void 사각형ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // g = panleDraw.CreateGraphics();

            
            //g.DrawRectangle(new Pen(drawFigure.Color), r);

            //체크표시 나타냄, 선택된 항목 checkedmenu변수에 이름 저장
            ToolStripMenuItem item = (ToolStripMenuItem)sender;
            foreach (ToolStripMenuItem it in item.Owner.Items)
            {
                if (it == item) //선택한 아이템에만 체크표시
                {
                    it.Checked = true; //클릭한 메뉴만 checked를 true로
                    checkedmenu = it.Name;
                }
                else
                {
                    it.Checked = false;
                }
            }

            //판넬위에 보여주기 위함
            panleDraw.Invalidate();
            panleDraw.Update();
            count++;
        }

       /* private void 타원ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            g = panleDraw.CreateGraphics();

            Rectangle r = new Rectangle(200, 50, 80, 150);
            g.DrawEllipse(drawFigure, r);

            count++;
        }
        
        private void 폐곡ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            g = panleDraw.CreateGraphics();

            Point[] pts =
            {
                new Point(115 +100, 30+100), new Point(140+100, 90+100),
                new Point(200+100, 115+100), new Point(140+100, 140+100),
                new Point(115+100, 200+100), new Point(90+100, 140+100),
                new Point(30+100, 115+100), new Point(90+100, 90+100)
            };

            g.DrawClosedCurve(drawFigure, pts);

            count++;
        }

        private void 곡선ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            g = panleDraw.CreateGraphics();

            Point[] pts =
            {
                new Point(40, 100), new Point(50, 60),
                new Point(60, 50), new Point(70, 60),
                new Point(80, 100), new Point(90, 140),
                new Point(100, 150), new Point(110, 140),
                new Point(120, 100), new Point(130, 60),
                new Point(140, 50), new Point(150, 60),
                new Point(160, 100), new Point(170, 140),
                new Point(180, 150), new Point(190, 140),
                new Point(200, 100)
            };

            g.DrawCurve(drawFigure, pts);

            count++;
        }*/

        private void 저장ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            saveFileDialog1.InitialDirectory = @"C:\";
            saveFileDialog1.Filter = "이미지파일(*.jpg)|*.jpg|이미지파일(*.png)|*.png|모든파일(*.*)|*.*";
            saveFileDialog1.FilterIndex = 1;

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                MySave(saveFileDialog1.FileName);
            }

            Close();
        }
        //이미지저장
        private void MySave(string str)
        {
            bmp.Save("panel.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
        }

        private void 종료ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if(count != 0)
            {
                DialogResult dr = MessageBox.Show("저장하시겠습니까?","안내",MessageBoxButtons.YesNo,MessageBoxIcon.Asterisk);

                if(dr == DialogResult.Yes)
                {
                    저장ToolStripMenuItem_Click( sender, e );
                }
            }
            Close();
        }

        //paint도구를 사용해 그리기
        private void panleDraw_Paint(object sender, PaintEventArgs e)
        {
            
            Graphics pg = e.Graphics;

            if(checkedmenu == "선lineToolStripMenuItem") //선그리기
            {
                startPoint = new Point(downX, downY);
                endPoint = new Point(upX, upY);

                pg.DrawLine(drawFigure, startPoint, endPoint);

                //panleDraw.DrawToBitmap(bmp, r);
            }
            else if (checkedmenu == "사각형ToolStripMenuItem") //사각형그리기
            {
                r = new Rectangle(downX, downY, Math.Abs(downX - upX), Math.Abs(downY - upY));
                pg.DrawRectangle(new Pen(drawFigure.Color), r);

                //panleDraw.DrawToBitmap(bmp, r);
            }
            else if (checkedmenu == "원ToolStripMenuItem") //원그리기
            {
                r = new Rectangle(downX, downY, Math.Abs(downX - upX), Math.Abs(downY - upY));
                pg.DrawEllipse(drawFigure, r);

                //panleDraw.DrawToBitmap(bmp, r);
            }

            /*
            if (r.X == 0)
                return;
            pg.DrawRectangle(new Pen(drawFigure.Color), r);*/
            
        }

        private void panleDraw_MouseDown(object sender, MouseEventArgs e)
        {
            downX = e.X; downY = e.Y;
        }

        private void panleDraw_MouseUp(object sender, MouseEventArgs e)
        {
            upX = e.X; upY = e.Y;
            
        }
    }
}
