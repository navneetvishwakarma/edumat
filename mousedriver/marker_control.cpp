#include <cv.h>
#include <highgui.h>
#include <iostream>
#include <stdio.h>
#include <sys/time.h>
#include <X11/extensions/XTest.h>
extern "C"{
    #include "x11_event.h" //including mouse driver
}
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
Display* construct_display()
{
    Display *res;
    res = XOpenDisplay(NULL);
    if (!res)
    res = NULL;
    return res;
}
int destroy_display(Display *active_display)
{
    int res;
    res = XCloseDisplay(active_display);
    return res;
}
int send_event( int keycode, Display *active_display)
{
    int res = 0;
    XEvent event;
    Window win;
    int revert_to;
    struct timeval t;
    gettimeofday(&t, NULL);
    XGetInputFocus(active_display, &win, &revert_to);
    event.xkey.type = KeyPress;
    event.xkey.serial = 0;
    event.xkey.send_event = True;
    event.xkey.display = active_display;
    event.xkey.window = win;
    event.xkey.root = XDefaultRootWindow(active_display);
    event.xkey.subwindow = None;
    event.xkey.time = t.tv_usec;
    event.xkey.x = 0;
    event.xkey.y = 0;
    event.xkey.x_root = 0;
    event.xkey.state = 0;
    event.xkey.keycode = keycode;
    event.xkey.same_screen=True;
    res = XSendEvent(active_display, InputFocus, True, 3, &event);
    XFlush(active_display);
    if (res == BadValue || res == BadWindow)
    res = -1;
    return res;
}
int mouse_move(int x, int y, Display *active_display)
{
    int res = 0;
    Window win;
    int revert_to;
    static int is_xtest_available = -1;
    int ev, er, ma, mi;
    if (!active_display) {
        res = -1;
        return -1;
    }
    XGetInputFocus(active_display, &win, &revert_to);
    if (is_xtest_available == -1)
    is_xtest_available = XTestQueryExtension(active_display, &ev, &er, &ma, &mi);
    if (is_xtest_available)
    XTestFakeRelativeMotionEvent(active_display, x, y , CurrentTime);
    //flush events
    XFlush(active_display);
    if (res == BadValue || res == BadWindow)
    res = -1;
    return 1;
}
int mouse_move1(int x, int y, Display *active_display)
{
    int res = 0;
    Window win;
    int revert_to;
    static int is_xtest_available = -1;
    int ev, er, ma, mi;
    if (!active_display) {
        res = -1;
        return -1;
    }
    XGetInputFocus(active_display, &win, &revert_to);
    if (is_xtest_available == -1)
    is_xtest_available = XTestQueryExtension(active_display, &ev, &er, &ma, &mi);
    if (is_xtest_available)
    XTestFakeMotionEvent(active_display,DefaultScreen(active_display), x, y,
    CurrentTime);
    //flush events
    XFlush(active_display);
    if (res == BadValue || res == BadWindow)
    res = -1;
    return 1;
}
int mouse_click(int mouse_button, int button_status, Display *active_display)
{
    int result = -1;
    static int is_xtest_available = -1;
    int ev, er, ma, mi;
    int revert_to;
    Window win;
    if (is_xtest_available == -1) {
        is_xtest_available = XTestQueryExtension(active_display, &ev, &er, &ma, &mi);
    }
    if (is_xtest_available) {
        XGetInputFocus(active_display, &win, &revert_to);
        if (mouse_button == MOUSE_BUTTON_LEFT && button_status == MOUSE_BUTTON_PRESS) {
            XTestFakeButtonEvent(active_display, 1, True, CurrentTime);
        } else if (mouse_button == MOUSE_BUTTON_LEFT && button_status == MOUSE_BUTTON_RELEASE) {
            XTestFakeButtonEvent(active_display, 1, False, CurrentTime);
        } else if (mouse_button == MOUSE_BUTTON_MIDDLE && button_status == MOUSE_BUTTON_PRESS) {
            XTestFakeButtonEvent(active_display, 2, True, CurrentTime);
        } else if (mouse_button == MOUSE_BUTTON_MIDDLE && button_status == MOUSE_BUTTON_RELEASE) {
            XTestFakeButtonEvent(active_display, 2, False, CurrentTime);
        } else if (mouse_button == MOUSE_BUTTON_RIGHT && button_status == MOUSE_BUTTON_PRESS) {
            XTestFakeButtonEvent(active_display, 3, True, CurrentTime);
        } else if (mouse_button == MOUSE_BUTTON_RIGHT && button_status == MOUSE_BUTTON_RELEASE) {
            XTestFakeButtonEvent(active_display, 3, False, CurrentTime);
        } else if (mouse_button == MOUSE_SCROLL_UP) {
            XTestFakeButtonEvent(active_display, 4, True, CurrentTime);
            XTestFakeButtonEvent(active_display, 4, False, CurrentTime);
        } else if (mouse_button == MOUSE_SCROLL_DOWN) {
            XTestFakeButtonEvent(active_display, 5, True, CurrentTime);
            XTestFakeButtonEvent(active_display, 5, False, CurrentTime);
        }
        XFlush(active_display);
        result = 0;
    } else {
        perror("Cannot create mouse click events\n");
    }
    return result;
}
int cam() //calling main
{
    int hdims = 16;
    printf("I am main");
    CvCapture* capture = cvCreateCameraCapture(1); //determining usb camera
    CvHistogram *hist = 0;
    CvMemStorage* g_storage = NULL;
    Display *display=construct_display();
    int x,y, tmpx=0, tmpy=0, chk=0;
    IplImage* image=0;
    IplImage* lastimage1=0;
    IplImage* lastimage=0;
    IplImage* diffimage;
    IplImage* bitimage;
    IplImage* src=0,*hsv=0,*hue=0,*backproject=0;
    IplImage* hsv1=0,*hue1=0,*histimg=0,*frame=0,*edge=0;
    float* hranges;
    cvNamedWindow( "CA", CV_WINDOW_AUTOSIZE ); //display window 3
    //Calculation of Histogram//
    cvReleaseImage(&src);
    src= cvLoadImage("images/skin.jpg"); //taking patch
    while(1)
    {
        frame = cvQueryFrame( capture ); //taking frame by frame for image prcessing
        int j=0;
        float avgx=0;
        float avgy=0;
        if( !frame ) break;
        //#########################Background Substraction#########################//
        if(!image)
        {
            image=cvCreateImage(cvSize(frame->width,frame->height),frame->depth,1);
            bitimage=cvCreateImage(cvSize(frame->width,frame->height),frame->depth,1);
            diffimage=cvCreateImage(cvSize(frame->width,frame->height),frame->depth,1);
            lastimage=cvCreateImage(cvSize(frame->width,frame->height),frame->depth,1);
        }
        cvCvtColor(frame,image,CV_BGR2GRAY);
        if(!lastimage1)
        {
            lastimage1=cvLoadImage("images/img.jpg");
        }
        cvCvtColor(lastimage1,lastimage,CV_BGR2GRAY);
        cvAbsDiff(image,lastimage,diffimage);
        cvThreshold(diffimage,bitimage,65,225,CV_THRESH_BINARY);
        cvInRangeS(bitimage,cvScalar(0),cvScalar(30),bitimage);
        cvSet(frame,cvScalar(0,0,0),bitimage);
        cvReleaseImage(&hsv);
        hsv= cvCreateImage( cvGetSize(src), 8, 3 );
        cvReleaseImage(&hue);
        hue= cvCreateImage( cvGetSize(src), 8, 1);
        cvCvtColor(src,hsv,CV_BGR2HSV);
        cvSplit(hsv,hue,0,0,0);
        float hranges_arr[] = {0,180};
        hranges = hranges_arr;
        hist = cvCreateHist( 1, &hdims, CV_HIST_ARRAY, &hranges, 1 );
        cvCalcHist(&hue, hist, 0, 0 );
        cvThreshHist( hist, 100 );
        //#############################Display histogram##############################//
        cvReleaseImage(&histimg);
        histimg = cvCreateImage( cvSize(320,200), 8, 3 );
        cvZero( histimg );
        int bin_w = histimg->width / hdims;
        //#### Calculating the Probablity of Finding the skin with in-built method ###//
        if(0)
        {
            free (backproject);
            free (hsv1);
            free (hue1);
        }
        cvReleaseImage(&backproject);
        backproject= cvCreateImage( cvGetSize(frame), 8, 1 );
        cvReleaseImage(&hsv1);
        hsv1 = cvCreateImage( cvGetSize(frame), 8, 3);
        cvReleaseImage(&hue1);
        hue1 = cvCreateImage( cvGetSize(frame), 8, 1);
        cvCvtColor(frame,hsv1,CV_BGR2HSV);
        cvSplit(hsv1,hue1,0,0,0);
        cvCalcBackProject( &hue1, backproject, hist );
        cvSmooth(backproject,backproject,CV_GAUSSIAN);
        cvSmooth(backproject,backproject,CV_MEDIAN);
        if( g_storage == NULL )
        g_storage = cvCreateMemStorage(0);
        else
        cvClearMemStorage( g_storage );
        CvSeq* contours=0;
        CvSeq* result =0;
        cvFindContours(backproject, g_storage, &contours );
        if(contours)
        {
            result=cvApproxPoly(contours, sizeof(CvContour), g_storage,
            CV_POLY_APPROX_DP, 7, 1);
        }
        cvZero( backproject);
        for( ; result != 0; result = result->h_next )
        {
            double area = cvContourArea( result );
            cvDrawContours( backproject,result, CV_RGB(255,255, 255), CV_RGB(255,0, 255)
            , -1,CV_FILLED, 8 );
            for( int i=1; i<=result-> total; i++ )
            {
                if(i>=1 and abs(area)>300)
                {
                    CvPoint* p2 = CV_GET_SEQ_ELEM( CvPoint, result, i );
                    if(1)
                    {
                        avgx=avgx+p2->x;
                        avgy=avgy+p2->y;
                        j=j+1;
                        cvCircle(backproject,cvPoint(p2->x,p2->y ),10,
                        cvScalar(255,255,255));
                    }
                }
            }
        }
        cvCircle( backproject, cvPoint(avgx/j, avgy/j ), 40, cvScalar(255,255,255) );
        x = ( avgx/j );
        y = ( avgy/j );
        x=( (x*1240)/640 )-20;
        y=( (y*840)/480 )-20;
        if ( (abs(tmpx-x)>6 or abs(tmpy-y)>6 ) and j )
        {
            tmpx = x;
            tmpy = y;
            chk=0;
        }
        else chk++;
        mouse_move1( tmpx, tmpy, display );
        if ( chk==10 )
        {
            mouse_click( 5, 2, display );
            mouse_click( 5, 3, display );
        }
        cvSaveImage( "final.jpg", frame );
        cvSaveImage( "final1.jpg", backproject );
        cvShowImage( "CA", backproject );
        char c = cvWaitKey(33);
        if( c == 27 )
        break; //function break and destroying windows if press <escape> key
    }
    cvReleaseCapture( &capture );
    cvDestroyWindow( "CA" );
}
