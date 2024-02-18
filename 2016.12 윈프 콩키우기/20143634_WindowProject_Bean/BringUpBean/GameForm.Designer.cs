namespace BringUpBean
{
    partial class GameForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(GameForm));
            this.btnGameEnd = new System.Windows.Forms.Button();
            this.picBerry = new System.Windows.Forms.PictureBox();
            this.picPeach = new System.Windows.Forms.PictureBox();
            this.picApple = new System.Windows.Forms.PictureBox();
            this.raBtnBerry = new System.Windows.Forms.RadioButton();
            this.raBtnPeach = new System.Windows.Forms.RadioButton();
            this.raBtnApple = new System.Windows.Forms.RadioButton();
            this.btnGameStart = new System.Windows.Forms.Button();
            this.panelSelect = new System.Windows.Forms.Panel();
            this.picBoxLine = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picBerry)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picPeach)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picApple)).BeginInit();
            this.panelSelect.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picBoxLine)).BeginInit();
            this.SuspendLayout();
            // 
            // btnGameEnd
            // 
            this.btnGameEnd.Location = new System.Drawing.Point(267, 483);
            this.btnGameEnd.Name = "btnGameEnd";
            this.btnGameEnd.Size = new System.Drawing.Size(140, 39);
            this.btnGameEnd.TabIndex = 0;
            this.btnGameEnd.Text = "콩에게돌아가기";
            this.btnGameEnd.UseVisualStyleBackColor = true;
            this.btnGameEnd.Click += new System.EventHandler(this.btnGameEnd_Click);
            // 
            // picBerry
            // 
            this.picBerry.BackColor = System.Drawing.SystemColors.Control;
            this.picBerry.Image = ((System.Drawing.Image)(resources.GetObject("picBerry.Image")));
            this.picBerry.Location = new System.Drawing.Point(120, 49);
            this.picBerry.Name = "picBerry";
            this.picBerry.Size = new System.Drawing.Size(130, 120);
            this.picBerry.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picBerry.TabIndex = 1;
            this.picBerry.TabStop = false;
            // 
            // picPeach
            // 
            this.picPeach.BackColor = System.Drawing.SystemColors.Control;
            this.picPeach.Image = ((System.Drawing.Image)(resources.GetObject("picPeach.Image")));
            this.picPeach.Location = new System.Drawing.Point(120, 191);
            this.picPeach.Name = "picPeach";
            this.picPeach.Size = new System.Drawing.Size(130, 120);
            this.picPeach.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picPeach.TabIndex = 2;
            this.picPeach.TabStop = false;
            // 
            // picApple
            // 
            this.picApple.BackColor = System.Drawing.SystemColors.Control;
            this.picApple.Image = ((System.Drawing.Image)(resources.GetObject("picApple.Image")));
            this.picApple.Location = new System.Drawing.Point(120, 343);
            this.picApple.Name = "picApple";
            this.picApple.Size = new System.Drawing.Size(130, 120);
            this.picApple.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picApple.TabIndex = 3;
            this.picApple.TabStop = false;
            // 
            // raBtnBerry
            // 
            this.raBtnBerry.AutoSize = true;
            this.raBtnBerry.Location = new System.Drawing.Point(16, 28);
            this.raBtnBerry.Name = "raBtnBerry";
            this.raBtnBerry.Size = new System.Drawing.Size(58, 19);
            this.raBtnBerry.TabIndex = 4;
            this.raBtnBerry.Text = "딸기";
            this.raBtnBerry.UseVisualStyleBackColor = true;
            // 
            // raBtnPeach
            // 
            this.raBtnPeach.AutoSize = true;
            this.raBtnPeach.Location = new System.Drawing.Point(16, 164);
            this.raBtnPeach.Name = "raBtnPeach";
            this.raBtnPeach.Size = new System.Drawing.Size(73, 19);
            this.raBtnPeach.TabIndex = 5;
            this.raBtnPeach.Text = "복숭아";
            this.raBtnPeach.UseVisualStyleBackColor = true;
            // 
            // raBtnApple
            // 
            this.raBtnApple.AutoSize = true;
            this.raBtnApple.Location = new System.Drawing.Point(16, 315);
            this.raBtnApple.Name = "raBtnApple";
            this.raBtnApple.Size = new System.Drawing.Size(58, 19);
            this.raBtnApple.TabIndex = 6;
            this.raBtnApple.Text = "사과";
            this.raBtnApple.UseVisualStyleBackColor = true;
            // 
            // btnGameStart
            // 
            this.btnGameStart.Location = new System.Drawing.Point(120, 483);
            this.btnGameStart.Name = "btnGameStart";
            this.btnGameStart.Size = new System.Drawing.Size(129, 39);
            this.btnGameStart.TabIndex = 7;
            this.btnGameStart.Text = "시작!";
            this.btnGameStart.UseVisualStyleBackColor = true;
            this.btnGameStart.Click += new System.EventHandler(this.btnGameStart_Click);
            // 
            // panelSelect
            // 
            this.panelSelect.Controls.Add(this.raBtnApple);
            this.panelSelect.Controls.Add(this.raBtnPeach);
            this.panelSelect.Controls.Add(this.raBtnBerry);
            this.panelSelect.Location = new System.Drawing.Point(8, 71);
            this.panelSelect.Name = "panelSelect";
            this.panelSelect.Size = new System.Drawing.Size(97, 365);
            this.panelSelect.TabIndex = 8;
            // 
            // picBoxLine
            // 
            this.picBoxLine.Image = ((System.Drawing.Image)(resources.GetObject("picBoxLine.Image")));
            this.picBoxLine.Location = new System.Drawing.Point(620, 49);
            this.picBoxLine.Name = "picBoxLine";
            this.picBoxLine.Size = new System.Drawing.Size(30, 414);
            this.picBoxLine.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picBoxLine.TabIndex = 10;
            this.picBoxLine.TabStop = false;
            // 
            // GameForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(752, 561);
            this.Controls.Add(this.picApple);
            this.Controls.Add(this.picPeach);
            this.Controls.Add(this.picBerry);
            this.Controls.Add(this.panelSelect);
            this.Controls.Add(this.btnGameStart);
            this.Controls.Add(this.btnGameEnd);
            this.Controls.Add(this.picBoxLine);
            this.Name = "GameForm";
            this.Text = "과일 경주 게임";
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.GameForm_MouseMove);
            ((System.ComponentModel.ISupportInitialize)(this.picBerry)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picPeach)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picApple)).EndInit();
            this.panelSelect.ResumeLayout(false);
            this.panelSelect.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picBoxLine)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnGameEnd;
        private System.Windows.Forms.PictureBox picBerry;
        private System.Windows.Forms.PictureBox picPeach;
        private System.Windows.Forms.PictureBox picApple;
        private System.Windows.Forms.RadioButton raBtnBerry;
        private System.Windows.Forms.RadioButton raBtnPeach;
        private System.Windows.Forms.RadioButton raBtnApple;
        private System.Windows.Forms.Button btnGameStart;
        private System.Windows.Forms.Panel panelSelect;
        private System.Windows.Forms.PictureBox picBoxLine;
    }
}