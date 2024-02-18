package com.example.a151228.webviewtest;

import android.content.Context;
import android.content.DialogInterface;
import android.os.Handler;
import android.provider.Browser;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.JavascriptInterface;
import android.webkit.JsResult;
import android.webkit.WebBackForwardList;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity {

    private WebView webView;
    private Handler mHandler = new Handler();
    final Context myApp = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webView = (WebView)findViewById(R.id.webview);

        webView.dispatchWindowFocusChanged(true);
        webView.dispatchSetSelected(true);
        webView.setFocusable(true);
        webView.setFocusableInTouchMode(false);
        webView.setVerticalFadingEdgeEnabled(true);
        webView.setVerticalScrollBarEnabled(true);
        webView.setScrollBarStyle(WebView.SCROLLBARS_OUTSIDE_OVERLAY);

        WebSettings webSettings = webView.getSettings();
        webSettings.setSavePassword(false);
        webSettings.setSaveFormData(false);
        webSettings.setJavaScriptEnabled(true);
        webSettings.setSupportZoom(false);
        webSettings.setSupportMultipleWindows(true);
        webSettings.setGeolocationEnabled(true);
        webSettings.setJavaScriptCanOpenWindowsAutomatically(true);
        webSettings.setBuiltInZoomControls(true);

        // Setting Local Storage
        webSettings.setDatabaseEnabled(true);
        webSettings.setDomStorageEnabled(true);

       // webView.setWebViewClient(new WebViewClientClass());
        webView.setWebChromeClient(new WebChromeClient(){
            @Override
            public boolean onJsAlert(WebView view, String url, String message, final android.webkit.JsResult result) {
                new AlertDialog.Builder(myApp)
                        .setTitle("Alert")
                        .setMessage(message)
                        .setPositiveButton(android.R.string.ok,
                                new AlertDialog.OnClickListener() {
                                    public void onClick(DialogInterface dialog, int which) {
                                        result.confirm();
                                    }
                                })
                        .setCancelable(false)
                        .create()
                        .show();

                return true;
            }

            @Override
            public boolean onCreateWindow(WebView view, boolean dialog, boolean userGesture, android.os.Message resultMsg) {
                view.removeAllViews();

                WebView childView = new WebView(view.getContext());
                childView.getSettings().setJavaScriptEnabled(true);
                childView.setWebChromeClient(this);
                childView.setWebViewClient(new WebViewClient());
                childView.setLayoutParams(new LinearLayout.LayoutParams(ActionBar.LayoutParams.FILL_PARENT, ActionBar.LayoutParams.FILL_PARENT));

                view.addView(childView);

                WebView.WebViewTransport transport = (WebView.WebViewTransport) resultMsg.obj;
                transport.setWebView(childView);
                resultMsg.sendToTarget();

                return true;
            }

            @Override
            public void onCloseWindow(WebView window) {
                super.onCloseWindow(window);
                webView.removeView(window);
            }

        });

        webView.addJavascriptInterface(new JavaScriptMethods(), "sample");
        webView.loadUrl("http://wldms7256.dothome.co.kr/getAPI/a_input.php");

    }



    final class JavaScriptMethods{
        JavaScriptMethods(){
        }

        //앱에서 정의한 메소드. 웹페이지에서 호출할 대상
        @android.webkit.JavascriptInterface
        public void clickOnFace(){
            //핸들러로 처리
            mHandler.post(new Runnable(){
                public void run(){
                    //웹페이지의 자바스크립트 함수 호출
                    webView.loadUrl("javascript:changeFace()");
                }
            });

        }
    }


}
