using System;
using UnityEngine;
using ZXing;

public class CameraController : MonoBehaviour
{
    private WebCamTexture cam;
    private Rect rectangle;

    void Start()
    {
        rectangle = new Rect(105, 50, 200, 200);
        cam = new WebCamTexture();
        cam.requestedHeight = 100;
        cam.requestedWidth = 100;

        if (cam != null)
        {
            cam.Play();
        }
    }

    void OnGUI()
    {
        GUI.DrawTexture(rectangle, cam, ScaleMode.ScaleToFit);

        try
        {
            IBarcodeReader codeReader = new BarcodeReader();

            var result = codeReader.Decode(cam.GetPixels32(),
              cam.width, cam.height);
            if (result != null)
            {
                Debug.Log("Your code for this product is: " +result.Text);
            }
        }
        catch (Exception e)
        {
            Debug.LogWarning(e.Message);
        }
    }
}