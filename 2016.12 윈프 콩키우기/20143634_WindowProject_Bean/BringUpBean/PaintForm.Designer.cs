namespace BringUpBean
{
    partial class PaintForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.파일ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.저장ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.종료ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.그리기ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.선lineToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.사각형ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.원ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.펜ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.색ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.굵기1ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.굵기3ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.굵기5ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.굵기10ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.panleDraw = new System.Windows.Forms.Panel();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.파일ToolStripMenuItem,
            this.그리기ToolStripMenuItem,
            this.펜ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(503, 28);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 파일ToolStripMenuItem
            // 
            this.파일ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.저장ToolStripMenuItem,
            this.종료ToolStripMenuItem});
            this.파일ToolStripMenuItem.Name = "파일ToolStripMenuItem";
            this.파일ToolStripMenuItem.Size = new System.Drawing.Size(51, 24);
            this.파일ToolStripMenuItem.Text = "파일";
            // 
            // 저장ToolStripMenuItem
            // 
            this.저장ToolStripMenuItem.Name = "저장ToolStripMenuItem";
            this.저장ToolStripMenuItem.Size = new System.Drawing.Size(114, 26);
            this.저장ToolStripMenuItem.Text = "저장";
            this.저장ToolStripMenuItem.Click += new System.EventHandler(this.저장ToolStripMenuItem_Click);
            // 
            // 종료ToolStripMenuItem
            // 
            this.종료ToolStripMenuItem.Name = "종료ToolStripMenuItem";
            this.종료ToolStripMenuItem.Size = new System.Drawing.Size(114, 26);
            this.종료ToolStripMenuItem.Text = "종료";
            this.종료ToolStripMenuItem.Click += new System.EventHandler(this.종료ToolStripMenuItem_Click);
            // 
            // 그리기ToolStripMenuItem
            // 
            this.그리기ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.선lineToolStripMenuItem,
            this.사각형ToolStripMenuItem,
            this.원ToolStripMenuItem});
            this.그리기ToolStripMenuItem.Name = "그리기ToolStripMenuItem";
            this.그리기ToolStripMenuItem.Size = new System.Drawing.Size(66, 24);
            this.그리기ToolStripMenuItem.Text = "그리기";
            // 
            // 선lineToolStripMenuItem
            // 
            this.선lineToolStripMenuItem.Name = "선lineToolStripMenuItem";
            this.선lineToolStripMenuItem.Size = new System.Drawing.Size(181, 26);
            this.선lineToolStripMenuItem.Tag = "1";
            this.선lineToolStripMenuItem.Text = "선";
            this.선lineToolStripMenuItem.Click += new System.EventHandler(this.선lineToolStripMenuItem_Click);
            // 
            // 사각형ToolStripMenuItem
            // 
            this.사각형ToolStripMenuItem.Name = "사각형ToolStripMenuItem";
            this.사각형ToolStripMenuItem.Size = new System.Drawing.Size(181, 26);
            this.사각형ToolStripMenuItem.Tag = "2";
            this.사각형ToolStripMenuItem.Text = "사각형";
            this.사각형ToolStripMenuItem.Click += new System.EventHandler(this.사각형ToolStripMenuItem_Click);
            // 
            // 원ToolStripMenuItem
            // 
            this.원ToolStripMenuItem.Name = "원ToolStripMenuItem";
            this.원ToolStripMenuItem.Size = new System.Drawing.Size(181, 26);
            this.원ToolStripMenuItem.Tag = "3";
            this.원ToolStripMenuItem.Text = "원";
            this.원ToolStripMenuItem.Click += new System.EventHandler(this.원ToolStripMenuItem_Click);
            // 
            // 펜ToolStripMenuItem
            // 
            this.펜ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.색ToolStripMenuItem,
            this.굵기1ToolStripMenuItem,
            this.굵기3ToolStripMenuItem,
            this.굵기5ToolStripMenuItem,
            this.굵기10ToolStripMenuItem});
            this.펜ToolStripMenuItem.Name = "펜ToolStripMenuItem";
            this.펜ToolStripMenuItem.Size = new System.Drawing.Size(36, 24);
            this.펜ToolStripMenuItem.Text = "펜";
            // 
            // 색ToolStripMenuItem
            // 
            this.색ToolStripMenuItem.Name = "색ToolStripMenuItem";
            this.색ToolStripMenuItem.Size = new System.Drawing.Size(135, 26);
            this.색ToolStripMenuItem.Text = "색";
            this.색ToolStripMenuItem.Click += new System.EventHandler(this.색ToolStripMenuItem_Click);
            // 
            // 굵기1ToolStripMenuItem
            // 
            this.굵기1ToolStripMenuItem.Name = "굵기1ToolStripMenuItem";
            this.굵기1ToolStripMenuItem.Size = new System.Drawing.Size(135, 26);
            this.굵기1ToolStripMenuItem.Text = "굵기 1";
            this.굵기1ToolStripMenuItem.Click += new System.EventHandler(this.굵기1ToolStripMenuItem_Click);
            // 
            // 굵기3ToolStripMenuItem
            // 
            this.굵기3ToolStripMenuItem.Name = "굵기3ToolStripMenuItem";
            this.굵기3ToolStripMenuItem.Size = new System.Drawing.Size(135, 26);
            this.굵기3ToolStripMenuItem.Text = "굵기 3";
            this.굵기3ToolStripMenuItem.Click += new System.EventHandler(this.굵기3ToolStripMenuItem_Click);
            // 
            // 굵기5ToolStripMenuItem
            // 
            this.굵기5ToolStripMenuItem.Name = "굵기5ToolStripMenuItem";
            this.굵기5ToolStripMenuItem.Size = new System.Drawing.Size(135, 26);
            this.굵기5ToolStripMenuItem.Text = "굵기 5";
            this.굵기5ToolStripMenuItem.Click += new System.EventHandler(this.굵기5ToolStripMenuItem_Click);
            // 
            // 굵기10ToolStripMenuItem
            // 
            this.굵기10ToolStripMenuItem.Name = "굵기10ToolStripMenuItem";
            this.굵기10ToolStripMenuItem.Size = new System.Drawing.Size(135, 26);
            this.굵기10ToolStripMenuItem.Text = "굵기 10";
            this.굵기10ToolStripMenuItem.Click += new System.EventHandler(this.굵기10ToolStripMenuItem_Click);
            // 
            // panleDraw
            // 
            this.panleDraw.BackColor = System.Drawing.Color.White;
            this.panleDraw.Location = new System.Drawing.Point(16, 40);
            this.panleDraw.Name = "panleDraw";
            this.panleDraw.Size = new System.Drawing.Size(473, 418);
            this.panleDraw.TabIndex = 1;
            this.panleDraw.Paint += new System.Windows.Forms.PaintEventHandler(this.panleDraw_Paint);
            this.panleDraw.MouseDown += new System.Windows.Forms.MouseEventHandler(this.panleDraw_MouseDown);
            this.panleDraw.MouseUp += new System.Windows.Forms.MouseEventHandler(this.panleDraw_MouseUp);
            // 
            // PaintForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(503, 470);
            this.Controls.Add(this.menuStrip1);
            this.Controls.Add(this.panleDraw);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "PaintForm";
            this.Text = "PaintForm";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 파일ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 저장ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 그리기ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 펜ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 종료ToolStripMenuItem;
        private System.Windows.Forms.Panel panleDraw;
        private System.Windows.Forms.ToolStripMenuItem 선lineToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 사각형ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 색ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 굵기1ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 굵기3ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 굵기5ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 굵기10ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 원ToolStripMenuItem;
    }
}