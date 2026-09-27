import Foundation
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count > 1 else { print("usage: ocr <image>"); exit(2) }
for path in args.dropFirst() {
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        FileHandle.standardError.write("FAIL load \(path)\n".data(using:.utf8)!); continue
    }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = true
    req.recognitionLanguages = ["zh-Hant","zh-Hans","en-US"]
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    do {
        try handler.perform([req])
        let obs = (req.results ?? []).compactMap { $0.topCandidates(1).first }
        print("=== \((path as NSString).lastPathComponent) ===")
        if obs.isEmpty { print("  (no text detected)") }
        for o in obs {
            let s = o.string
            let bad = ["鷦鯨","鵎鶓","鶕鵃","鵜鶘","鵜鵠","鸟","鴕","鵜鷕","鵜鶋","鹤","鷺","鵝"]
            let flags = bad.filter { s.contains($0) }.map { "\($0)✓" }
            print("  [\(String(format:"%.2f", o.confidence))] \(s)\(flags.isEmpty ? "" : "   << \(flags.joined(separator:","))")")
        }
    } catch { print("FAIL perform \(path): \(error)") }
}
